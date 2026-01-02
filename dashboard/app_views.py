from django.http import JsonResponse


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
