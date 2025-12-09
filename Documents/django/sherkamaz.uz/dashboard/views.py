
from django.contrib.auth.decorators  import login_required 
from django.shortcuts import render
# ensuring the login page is not cached 




   
@login_required(login_url = "accounts:login")

def home(request):
	show_login_toast = request.session.pop("show_login_toast","")
	request_height = request.POST.get("height_cm")
	request_weight =request.POST.get("weight_kg")
	request_age = request.POST.get("age")
	request_waist = request.POST.getlist("gender",None)[0]
	print(request_waist)

	height_cm = int(request_height) if request_height not in (None, "", "None") and str(request_height).strip().isdigit() else None
	 
	weight_kg = int(request_weight) if request_weight not in (None,"","None") and str(request_weight).strip().isdigit() else None

	# age = int(request.POST.get("age")) if request.POST.get("age") is not "" else None
	age = int(request_age) if request_age not in (None,"","None") and str(request_age).strip().isdigit() else None

	waist = int(request_waist) if request_waist not in (None,"","None") and str(request_waist).strip().isdigit() else None
	# waist = int(request.POST.get("waist")) if request.POST.get("waist") is not "" else None
	if(height_cm  is not None and weight_kg  is not None and age is not None  and waist is not None):
		calculateAnthropoAge(request,height_cm,weight_kg,age,waist)
	return render(request,"dashboard/main.html",{"show_toast":show_login_toast})





def calculateAnthropoAge(request,height_cm,weight_kg,age,waist):
	bmiStatus = ""
	bmiImage = '';
	bmi =  round(weight_kg / ((height_cm / 100) ** 2), 1) if height_cm > 0  else None
	if(bmi <18.5):
		bmiStatus = "You are underweight"
	elif bmi < 25:
		bmiStatus = "You are healthy"
	else:
		bmiStatus = "You are overweight"

	print(bmiStatus)	
	bmi = weight_kg /((height_cm / 100) ** 2)
	waist_ratio = waist / height_cm
	idealBMI = 22
	sex =waist
	print(sex)
	

	return render(request,"dashboard/main.html",{"bmiStatus":bmiStatus})

# Create your views here.

