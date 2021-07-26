import itertools

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from organizations.models import Organization


class ListOrganization(ListView):
    model = Organization
    template_name = 'organizations/organization_list.html'
    extra_context = {
        'page_title': 'Organizations'
    }

    def get_queryset(self):
        super(ListOrganization, self).get_queryset()
        if self.request.user.is_authenticated:
            user_organizations = Organization.objects.filter(submit_user=self.request.user)
            other_organizations = Organization.objects.exclude(submit_user=self.request.user)
        else:
            user_organizations = Organization.objects.all()
            other_organizations = []
        qs = list(itertools.chain(user_organizations, other_organizations))
        return qs


class CreateOrganization(PermissionRequiredMixin, CreateView):
    model = Organization
    fields = ('province', 'name', 'organization_phone', 'number_of_workers', 'products', 'owner_of_organization',
              'owner_phone', 'owner_email')
    success_url = reverse_lazy('organizations:list-organizations')
    extra_context = {
        'page_title': 'Create an Organization'
    }
    permission_required = 'organizations.add_organization'

    def form_valid(self, form):
        form.instance.submit_user = self.request.user
        return super(CreateOrganization, self).form_valid(form)
