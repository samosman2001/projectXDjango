from django.shortcuts import render
from django.http import JsonResponse
from .models import Nutrition, LogFood
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
def nutrition(request):
	return render(request,"nutrition/nutrition.html")

@login_required
def get_food_logs(request):
    logs = LogFood.objects.filter(user=request.user).select_related("food").order_by("-created_at")

    data = []
    for log in logs:
        data.append({
            "time": log.created_at.strftime("%H:%M"),
            "name": log.food.name,
            "protein": log.protein,
            "carbs": log.carbs,
            "fat": log.fat,
            "calories": log.calories,
        })

    return JsonResponse({"success": True, "logs": data})
