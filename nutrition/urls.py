from django.urls import path
from . import views   # import your views from the same folder
from . import app_views
app_name = "nutrition"
urlpatterns=[
  
 path("nutrition/",views.nutrition,name="nutrition"),
 path("app/getFoods/", app_views.get_foods),
 path("app/logFood/", app_views.log_food),
 path("get-food-logs/", views.get_food_logs)
] 