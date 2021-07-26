from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView


class Login(LoginView):
    def get_context_data(self, **kwargs):
        super(Login, self).get_context_data()
        context = {'page_title': 'login'}
        return context


def logout_view(request):
    logout(request)
    return redirect('organizations:list-organizations')


class EditUserProfile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ('first_name', 'last_name', 'email')
    success_url = reverse_lazy('organizations:list-organizations')
    extra_context = {
        'page_title': 'Edit Profile'
    }

    def get_object(self, queryset=None):
        return self.request.user
