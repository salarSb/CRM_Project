from django.urls import path

from . import views

app_name = 'organizations'
urlpatterns = [
    path('', views.hello, name='hello'),
    path('create/', views.CreateOrganization.as_view(), name='create-organization'),
]
