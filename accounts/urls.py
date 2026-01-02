from django.urls import path
from . import views   # import your views from the same folder
from . import app_views
app_name = "accounts"

urlpatterns = [
path("logout/",views.logout_view,name="logout"),
path("login/",views.login_view, name="login"),
path('register/', views.register, name='register'),
path("app/login/",app_views.app_login,name = "app_login"),
path("app/logout/",app_views.app_logout,name ="app_logout"),
path("app/verify_email_otp/",app_views.verify_email_otp,name ="verify_email_otp"),
path("app/request_email_otp/",app_views.request_email_otp,name ="request_email_otp"),
]