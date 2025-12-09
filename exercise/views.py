from django.shortcuts import render

def exercise(request):
	return render(request,"exercise/exercise.html")