from django.urls import path

from . import views

urlpatterns = [
    path("auth/register", views.register, name="register"),
    path("auth/login", views.login, name="login"),
    path("auth/login_user", views.login_user, name="login_user"),
    path("auth/logout", views.logout, name="logout"),
]
