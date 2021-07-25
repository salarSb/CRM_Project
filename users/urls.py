from django.urls import path

from users.views import Login, logout_view

app_name = 'users'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
