import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django .contrib.auth.decorators import login_required
from .models import Exercise,WorkoutLog,WorkoutPlan,WorkoutPlanExercise,WorkoutPlanSet
from nutrition.models import LogFood
from dashboard.models import UserMetrics
@login_required
def get_exercise(request):
	exercises = Exercise.objects.filter(is_active = True).values("id","name","mode")

	return JsonResponse({
		"success" : True,
		"exercise" :list(exercises)

		})
@login_required
@csrf_exempt

def log_exercise(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST required"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)
    print(data)
    plan_name = data.get("plan_name", "My Workout Plan")
    mode = data.get("mode", "home")
    exercises = data.get("exercises")

    if not isinstance(exercises, list):
        return JsonResponse({"success": False, "error": "Exercises must be a list"}, status=400)

    # 1️⃣ Create plan
    plan = WorkoutPlan.objects.create(
        user=request.user,
        name=plan_name,
        mode=mode
    )

    # 2️⃣ Create exercises + sets
    for idx, ex in enumerate(exercises):
        ex_name = ex.get("name")
        sets_list = ex.get("sets", [])

        if not ex_name:
            continue

        plan_ex = WorkoutPlanExercise.objects.create(
            plan=plan,
            exercise_name=ex_name,
            order=idx
        )

        for s in sets_list:
            WorkoutPlanSet.objects.create(
                plan_exercise=plan_ex,
                sets=int(s.get("sets", 0)),
                reps=int(s.get("reps", 0)),
                weight=float(s.get("weight", 0)),
                status=s.get("status", ""),
                mode=s.get("mode", mode),
            )
            WorkoutLog.objects.create(
            	user = request.user,
            	name = ex_name,
            	mode = s.get("mode",mode),
            	sets = s.get("sets",0),
            	reps = s.get("reps",0),
            	weight_kg = float(s.get("weight",0)),
            	calories = float(ex.get("calories",0)),
            	seconds = float(ex.get("seconds",0))
            	)

    return JsonResponse({
        "success": True,
        "plan_id": plan.id
    })
         
         
def getLastExercise(request):
	latest = (WorkoutLog.objects.filter(user=request.user).order_by("-created_at").first())
	if not latest:
		return JsonResponse({"success": False, "error": "No workouts found"})

	return JsonResponse({
        "success": True,
        "workout": {
            "id": latest.id,
            "exercise": latest.name ,
            "reps": latest.reps,
            "weight_kg": latest.weight_kg,
            "created_at": latest.created_at,
        }
    })
def getAgeAndWeight(request):
	ageAndWeight = UserMetrics.objects.all().values()
	return JsonResponse({"success":True,"userMetrics":{
		"id":ageAndWeight[0].get("id"),
		"user_id":ageAndWeight[0].get("user_id"),
		"weight_kg" : ageAndWeight[0].get("weight"),
		"created_at" : ageAndWeight[0].get("created_at")
		}})


