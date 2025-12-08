from django.urls import path
from . import views   # import your views from the same folder
app_name = "dashboard"
urlpatterns = [
    
    path("", views.home, name="home"),
    
  
]
