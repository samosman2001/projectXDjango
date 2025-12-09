from django.urls import path
from . import views   # import your views from the same folder
app_name = "accounts"

urlpatterns = [
path("logout/",views.logout_view,name="logout"),
path("login/",views.login_view, name="login"),
path('register/', views.register, name='register')
]