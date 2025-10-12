from django.urls import path
from . import views   # import your views from the same folder
app_name = "dashboard"
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("", views.home, name="home"),
    path("logout/",views.logout_view,name="logout"),
    path("nutrition/",views.nutrition,name="nutrition"),
    path("exercise/",views.exercise,name="exercise")
]
