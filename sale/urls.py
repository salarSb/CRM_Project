from django.urls import path

from . import views

app_name = 'sale'

urlpatterns = [
    path('quotes/', views.QuotesList.as_view(), name='quotes'),
    path('submit-quote/', views.CreateQuote.as_view(), name='submit-quote'),
    path('print-quote/<int:pk>/', views.PrintQuote.as_view(), name='print-quote'),
]
