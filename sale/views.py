import weasyprint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from sale.forms import QuoteItemForm
from sale.models import QuoteItem, Quote
from sale.tasks import send_email_task


class QuotesList(LoginRequiredMixin, ListView):
    model = Quote
    extra_context = {
        'page_title': 'Quotes'
    }

    def get_queryset(self):
        qs = super(QuotesList, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        return qs


class CreateQuote(PermissionRequiredMixin, CreateView):
    model = QuoteItem
    form_class = QuoteItemForm
    success_url = reverse_lazy('sale:quotes')
    extra_context = {
        'page_title': 'Submit Quote'
    }
    permission_required = ['sale.add_quote', 'sale.add_quoteitem']

    def get_form_kwargs(self):
        kwargs = super(CreateQuote, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        quote_instance = Quote.objects.create(owner=self.request.user)
        form.instance.quote = quote_instance
        return super(CreateQuote, self).form_valid(form)


class PrintQuote(LoginRequiredMixin, DetailView):
    model = Quote

    def get(self, request, *args, **kwargs):
        g = super(PrintQuote, self).get(request, *args, **kwargs)
        rendered_content = g.rendered_content
        pdf = weasyprint.HTML(string=rendered_content, base_url='http://127.0.0.1:8000/').write_pdf()
        response = HttpResponse(pdf, content_type='appLication/pdf')
        return response


@login_required
def send_quote_to_organization_by_email(request, pk):
    quote_instance = get_object_or_404(klass=Quote, pk=pk)
    content = render_to_string('sale/quote_detail.html', {'object': quote_instance})
    sender = request.user.username
    receiver_queryset = quote_instance.quoteitem_set.all()
    receiver = ''
    for item in receiver_queryset:
        receiver = item.organization.owner_email
    send_email_task(content, sender, receiver)
    messages.success(request, 'Email has been Sent')
    return redirect(reverse_lazy('sale:quotes'))
