from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserMetrics

def app_home(request):
	if not request.user.is_authenticated:
		return JsonResponse({
			"success":False,
			"error":"Permission Declined"
			},status = 401)

			
	return JsonResponse(
   	{
    "success":True,
    "message" : "Successfully Signed in"
   	})



@csrf_exempt
def save_metrics(request):
    if request.method == "POST":
        data = json.loads(request.body)

        age = data.get("age")
        weight = data.get("weight")

        UserMetrics.objects.create(
            user=request.user,
            age=age,
            weight=weight
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})
