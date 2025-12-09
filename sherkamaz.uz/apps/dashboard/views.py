from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators  import login_required 
from django.utils.http import url_has_allowed_host_and_scheme
from django.urls import reverse



def safe_redirect(request,next_url,default ="dashboard:home"):
	if next_url and url_has_allowed_host_and_scheme(next_url,
		allowed_hosts={request.get_host()},require_https = request.is_secure()):
		return redirect(next_url)
	return redirect(reverse(default));

	
# any time you call /login page dashboard/login.html page is called automatically 
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        next_url = request.POST.get("next") or request.GET.get("next")

        user = authenticate(request, password=password, email=email)
        if user is not None and user.is_active:
            login(request, user)
            request.session["show_login_toast"] = True
            
            return safe_redirect(request, next_url)
        return render(request, "dashboard/login.html",{"show_toast":"Invalid username or password"})

    return render(request, "dashboard/login.html")
    # anytime you call /logout page it opens dashboard/login.html ,which in turn calls /logout page and dashboard/login.html page
    # is called automatically 
def logout_view(request):
   logout(request);
   request.session["show_logout_toast"] = "Successfully Logged out"
   show_logout_toast = request.session.pop("show_logout_toast",False);

   return render(request,"dashboard/login.html",{"show_toast":show_logout_toast})
@login_required(login_url = "dashboard:login")
def home(request):
	show_login_toast = request.session.pop("show_login_toast",False)
	return render(request,"dashboard/main.html",{"show_toast":show_login_toast})
def nutrition(request):
	return render(request,"dashboard/nutrition.html")
def exercise(request):
	return render(request,"dashboard/exercise.html")



# Create your views here.
