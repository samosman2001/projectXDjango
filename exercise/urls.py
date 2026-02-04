from django.urls import path
from . import views   # import your views from the same folder
from . import app_views
app_name = "exercise"
urlpatterns=[
  path("exercise", views.exercise,name = "exercise"),
 path("app/log_exercise",app_views.log_exercise,name ="log_exercise"),
 path("app/getWorkouts",views.get_workouts,name="get_workouts"),
 path("app/getLastExercise",app_views.getLastExercise),
 path("app/getAgeAndWeight",app_views.getAgeAndWeight),
 path("getCaloriesInAndOut",views.getCaloriesInAndOut)

]   