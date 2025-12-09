from django.urls import path
from . import views   # import your views from the same folder
app_name = "nutrition"
urlpatterns=[
  
 path("nutrition/",views.nutrition,name="nutrition"),
] 