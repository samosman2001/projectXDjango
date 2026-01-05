import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django .contrib.auth.decorators import login_required
from .models import Exercise,WorkoutLogs

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
		return JsonResponse({"success":False,"error":"Post Method required "},status = 405)

	try:
		data = json.loads(request.body.decode("utf-8") or {})
		print(data)
	except json.JsonEncodeError:
		return JsonResponse({"success ": False,"error":"Invalid JSON"},status = 400)
	if not request.user.is_authenticated:
		return JsonResponse({"success": True,"error":"Unauthorized User"},status = 404)
	
	result = {}

	for item in data:
			reps = item['sets'][0]['reps']
			print(reps)		
	sets = int(data.get("Squats_sets",0))
	# reps = int(data.get("S",0))
	# weight_kg = data.get("weight",0)
	# mode = data.get("mode","Gym")
	# status = data.get("status",0)
	# calories = float(data.get("calories",0))
	workout = WorkoutLogs.objects.create(
    	user = request.user,
    	exercise = exercise,
    	mode = mode,
    	sets = sets ,
    	reps = reps,
    	weight_kg  = weight_kg,

    	)
	return JsonResponse({"success" : True,"workout_id":workout.id})