from django.urls import path

from . import views

app_name = 'sale'

urlpatterns = [
    path('quotes/', views.QuotesList.as_view(), name='quotes'),
    path('submit-quote/', views.CreateQuote.as_view(), name='submit-quote'),
    path('print-quote/<int:pk>/', views.PrintQuote.as_view(), name='print-quote'),
    path('send-email/<int:pk>/', views.send_quote_to_organization_by_email, name='send-email'),
    path('create-followup/', views.FollowUpCreateView.as_view(), name='create-followup'),
]
