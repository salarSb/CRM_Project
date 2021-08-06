from django.urls import path

from . import views

app_name = 'sale'

urlpatterns = [
    path('quotes/', views.QuotesList.as_view(), name='quotes'),
    path('submit-quote/', views.CreateQuote.as_view(), name='submit-quote'),
    path('print-quote/<int:pk>/', views.PrintQuote.as_view(), name='print-quote'),
    path('send-email/<int:pk>/', views.send_quote_to_organization_by_email, name='send-email'),
    path('followup/create/', views.FollowUpCreateView.as_view(), name='create-followup'),
    path('followup/list/', views.FollowUpListView.as_view(), name='followup-list'),
    path('followup/detail/<int:pk>/', views.FollowUpDetailView.as_view(), name='followup-detail'),
]
