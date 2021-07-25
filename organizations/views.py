from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from organizations.models import Organization


def hello(request):
    return render(request, 'organizations/organization_list.html',
                  {'hello': 'hello world', 'page_title': 'organizations'})


class CreateOrganization(PermissionRequiredMixin, CreateView):
    model = Organization
    fields = ('province', 'name', 'organization_phone', 'number_of_workers', 'products', 'owner_of_organization',
              'owner_phone', 'owner_email')
    success_url = reverse_lazy('organizations:hello')
    extra_context = {
        'page_title': 'Create an Organization'
    }
    permission_required = 'organizations.add_organization'

    def form_valid(self, form):
        form.instance.submit_user = self.request.user
        return super(CreateOrganization, self).form_valid(form)
