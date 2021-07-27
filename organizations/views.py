import itertools

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from organizations.models import Organization
from organizations.serializers import OrganizationSerializer


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


class UpdateOrganization(PermissionRequiredMixin, UpdateView):
    model = Organization
    fields = ('province', 'name', 'organization_phone', 'number_of_workers', 'products', 'owner_of_organization',
              'owner_phone', 'owner_email')
    success_url = reverse_lazy('organizations:list-organizations')
    extra_context = {
        'page_title': 'Update an Organization'
    }
    permission_required = 'organizations.change_organization'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.submit_user != self.request.user:
            return HttpResponseForbidden('You are not Allowed to Edit this Organization')
        else:
            return super(UpdateOrganization, self).dispatch(request, *args, **kwargs)


class DetailOrganization(DetailView):
    model = Organization
    extra_context = {
        'page_title': 'Organization Detail'
    }


"""
Django Rest FrameWork Views
"""


class OrganizationAPI(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super(OrganizationAPI, self).get_queryset()
        qs = qs.filter(submit_user=self.request.user)
        return qs


class OrganizationDetailAPI(RetrieveUpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super(OrganizationDetailAPI, self).get_queryset()
        qs = qs.filter(submit_user=self.request.user)
        return qs
