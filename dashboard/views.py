
from django.contrib.auth.decorators  import login_required 
from django.shortcuts import render
# ensuring the login page is not cached 




   
@login_required(login_url = "accounts:login")
def home(request):
	show_login_toast = request.session.pop("show_login_toast",False)
	return render(request,"dashboard/main.html",{"show_toast":show_login_toast})

# Create your views here.

