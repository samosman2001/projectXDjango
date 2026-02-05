from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import WorkoutLog
from nutrition.models import LogFood
import json


def exercise(request):

	return render(request,"exercise/exercise.html",{})

# exercise/views.py

@login_required
def get_workouts(request):
    workouts = WorkoutLog.objects.filter(user=request.user)\
        .order_by("-created_at")

    return JsonResponse({
        "success": True,
        "workouts": [
            {
                "id": w.id,
                "user_id": w.user_id,
                "name":w.name,
                "sets": w.sets,
                "reps": w.reps,
                "weight": w.weight_kg,
                "mode": w.mode,
                "created_at": w.created_at.strftime("%Y-%m-%d"),
            }
            for w in workouts
        ]
    })

# def csrf(request):
#     return JsonResponse({"detail": "CSRF cookie set"})

@csrf_exempt
def log_exercise(request):
	try:
		data = json.loads(request.body.decode("utf-8") or {})
	except json.JSONDecodeError:
		return JsonResponse({"success ": False,"error":"Invalid JSON"},status = 400)
	if not user.is_authenticated:
		return JsonResponse({"success": True,"error":"Unauthorized User"},status = 404)

def getCaloriesInAndOut(request):
        workouts = WorkoutLog.objects.filter(user = request.user)
        foods = LogFood.objects.filter(user=request.user)
        return JsonResponse({"success": True,"caloriesOut":[
            {"calories":w.calories,"created_at":w.created_at}
            for w in workouts],"caloriesIn":[{
           "calories":food.calories,"created_at":food.created_at
            } for food in foods]},status = 400)   