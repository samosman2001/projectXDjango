from django.urls import path
from . import views   # import your views from the same folder
from . import app_views

app_name = "dashboard"
urlpatterns = [
    
    path("", views.home, name="home"),
    path ("app/home/",app_views.app_home,name="app_home"),
    path("app/save-metrics", app_views.save_metrics, name="save_metrics"),

  
]
