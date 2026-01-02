from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def csrf(request):
    return JsonResponse({"detail": "CSRF cookie set"})

@csrf_exempt
def log_exercise(request):
	try:
		data = json.loads(request.body.decode("utf-8") or {})
	except json.JsonEncodeError:
		return JsonResponse({"success ": False,"error":"Invalid JSON"},status = 400)
	if not user.is_authenticated:
		return JsonResponse({"success": True,"error":"Unauthorized User"},status = 404)
