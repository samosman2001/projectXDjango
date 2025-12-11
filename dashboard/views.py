
from django.contrib.auth.decorators  import login_required 
from django.shortcuts import render
# ensuring the login page is not cached 




   
@login_required(login_url = "accounts:login")

def home(request):
	show_login_toast = request.session.pop("show_login_toast","")
	request_height = request.POST.get("height_cm")
	request_weight =request.POST.get("weight_kg")
	request_age = request.POST.get("age")
	request_waist = request.POST.get("waist")
	request_gender = request.POST.getlist("gender",[None])[0]
	request_gender = request_gender if request is not [] else []
	print(request_gender)

	height_sm = int(request_height) if request_height not in (None, "", "None") and str(request_height).strip().isdigit() else None
	 
	weight_kg = int(request_weight) if request_weight not in (None,"","None") and str(request_weight).strip().isdigit() else None

	# age = int(request.POST.get("age")) if request.POST.get("age") is not "" else None
	age = int(request_age) if request_age not in (None,"","None") and str(request_age).strip().isdigit() else None

	waist = int(request_waist) if request_waist not in (None,"","None") and str(request_waist).strip().isdigit() else None
	gender = request_gender if request_gender not in(None,"","None")  else None
		# waist = int(request.POST.get("waist")) if request.POST.get("waist") is not "" else None
	
	if all([height_sm, weight_kg, age, waist, gender]):
		 anthroAge = calculateAnthropoAge(height_sm,weight_kg,age,waist,gender)
		 bmi_status,bmi_image,bmi= calculateBMI(height_sm,weight_kg)	
		 bmi_percent = getBMIPercent(bmi)
		 print(bmi)
		 return render(request,
		 	"dashboard/main.html",
		 	{
		 	"anthroAge" : anthroAge,
		 	"bmi_status":bmi_status,
		 	"bmi_image":bmi_image,
		 	"height_sm": height_sm,
		 	"weight_kg" : weight_kg,
		 	"bmi":bmi,
		 	"bmi_percent":bmi_percent ,
		 	"waist":waist,
		 	"age" : age
		 	})
 
	return render(request,"dashboard/main.html",{"show_toast":show_login_toast})

def calculateBMI(height_sm,weight_kg):
	   bmiStatus = ""
	   bmiImage = '';
	   bmi =  round(weight_kg / ((height_sm / 100) ** 2), 1) if height_sm > 0  else None
	   if(bmi <18.5):
	   	bmiStatus = "You are underweight"
	   	bmiImage = "icons/Male-Clothes-thin.svg"
	   elif bmi < 25:
	   	bmiStatus = "You are healthy"
	   	bmiImage = "icons/Male-Clothes.svg"
	   else :
	   	bmiStatus = "You are overweight"
	   	bmiImage = "icons/Male-Clothes-overWeight2.png"

	   print(bmiStatus)
	   return [bmiStatus,bmiImage,bmi]

def calculateAnthropoAge(height_sm,weight_kg,age,waist,gender):
			
	bmi = weight_kg /((height_sm / 100) ** 2)
	waist_ratio = waist / height_sm
	idealBMI = 22
	idealWaistRatio = 0.45 if gender == "male" else 0.42

	bmi_penalty = abs(bmi - idealBMI)
	waist_penalty = max(0,waist_ratio - idealWaistRatio) * 100
	penalty_score = (bmi_penalty * 0.8) + (waist_penalty *1.2)
	anthroAge = age + penalty_score;
	
	return round(anthroAge, 1);

	

# Create your views here.
def getBMIPercent(bmi):
	min = 15
	max = 35
	if(bmi is 0 or bmi < min): 
		return 0
	if(bmi > max):
		return 100
	return round((bmi - min)/(max - min) * 100,1)

