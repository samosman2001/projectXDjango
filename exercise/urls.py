from django.urls import path
from . import views   # import your views from the same folder
app_name = "exercise"
urlpatterns=[
  path("csrf/", views.csrf,name = "csrf"),
 path("app/log_exercise",views.log_exercise,name ="log_exercise"),
]   