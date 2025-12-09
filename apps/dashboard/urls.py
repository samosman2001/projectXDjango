from django.urls import path
from . import views   # import your views from the same folder

urlpatterns = [
    path("", views.home_redirect, name="home_page"),
    path("login/", views.login_redirect, name="login_page"),
    path("main/", views.main_redirect, name="main_page"),
]
