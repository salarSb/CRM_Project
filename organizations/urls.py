from django.urls import path

from . import views

app_name = 'organizations'
urlpatterns = [
    path('', views.ListOrganization.as_view(), name='list-organizations'),
    path('create/', views.CreateOrganization.as_view(), name='create-organization'),

    # DRF URLs
    path('api/v1/organization/', views.OrganizationAPI.as_view(), name='organization-api'),
    path('api/v1/organization/<int:pk>/', views.OrganizationDetailAPI.as_view(), name='organization-detail-api'),
]
