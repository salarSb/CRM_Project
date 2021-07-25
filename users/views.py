from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


class Login(LoginView):
    def get_context_data(self, **kwargs):
        super(Login, self).get_context_data()
        context = {'page_title': 'login'}
        return context


def logout_view(request):
    logout(request)
    return redirect('organizations:hello')
