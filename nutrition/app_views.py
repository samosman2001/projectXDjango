
from django.http import JsonResponse
from .models import Nutrition, LogFood
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt

@login_required
def get_foods(request):
    foods = list(Nutrition.objects.values(
        "id",
        "name",
        "calories",
        "protein",
        "carbs",
        "fat"
    ))
    return JsonResponse({"success": True, "foods": foods})

@csrf_exempt
@login_required
def log_food(request):
    if request.method == "POST":
        data = json.loads(request.body)

        food_id = data.get("food_id")
        grams = data.get("grams")
        meal_type = data.get("meal_type")

        if not food_id or not grams:
            return JsonResponse({"success": False, "error": "Missing data"})

        grams = float(grams)

        food = Nutrition.objects.get(id=food_id)

        factor = grams / 100

        LogFood.objects.create(
            user=request.user,
            food=food,
            grams=grams,
            calories=food.calories * factor,
            protein=food.protein * factor,
            carbs=food.carbs * factor,
            fat=food.fat * factor,
            meal_type=meal_type
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})

