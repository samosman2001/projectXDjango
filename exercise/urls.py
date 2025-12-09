from django.urls import path
from . import views   # import your views from the same folder
app_name = "exercise"
urlpatterns=[
  
 path("exercise/",views.exercise,name="exercise"),
]   