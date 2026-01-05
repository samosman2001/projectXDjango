from django.urls import path
from . import views   # import your views from the same folder
from . import app_views
app_name = "exercise"
urlpatterns=[
  path("exercise", views.exercise,name = "exercise"),
 path("app/log_exercise",app_views.log_exercise,name ="log_exercise"),
]   