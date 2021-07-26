from django.urls import path

from . import views

app_name = 'organizations'
urlpatterns = [
    path('', views.ListOrganization.as_view(), name='list-organizations'),
    path('create/', views.CreateOrganization.as_view(), name='create-organization'),
]
