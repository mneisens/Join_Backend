from django.urls import path
from .views import register, user_login, guest_login, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('guest-login/', guest_login, name='guest-login'),
    path('logout/', logout_view, name='logout'),
]
