from django.shortcuts import render
from django.utils.http import url_has_allowed_host_and_scheme
from django.urls import reverse
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import CleanUserCreationForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
# to avoid caching the login page
from django.views.decorators.cache import never_cache
# Create your views here.
def safe_redirect(request,next_url,default ="dashboard:home"):

	if next_url and url_has_allowed_host_and_scheme(next_url,
		allowed_hosts={request.get_host()},require_https = request.is_secure()):
		return redirect(next_url)
	return redirect(reverse(default)); 
def register(request,show_register = True):
    user_exist = User.objects.filter(email = request.POST.get("email")).exists()
    if(request.method == "POST"):

        form = CleanUserCreationForm(request.POST)
        if (form.is_valid()):
            if(user_exist):
                return render(request,"accounts/register.html",{"show_toast" : "Already Registered"
                    ,"form":form})
            form.save()
            return render(request,"accounts/login.html",{"show_toast":"The user has successfully been registered"})
        else:
            
            return render(request,"accounts/register.html",
                {"show_toast" : "Fill up the fields correctly",
                "form" : form})
    else:
     form = CleanUserCreationForm() 
       
     return render(request,"accounts/register.html",
                {"form" : form})


# any time you call /login page dashboard/login.html page is called automatically 
@never_cache
def login_view(request):
    show_logout_toast =request.session.pop("show_logout_toast",True)
    if request.user.is_authenticated:
        return redirect("dashboard:home")
    if request.method == "POST":
        username = request.POST.get("login_email","").strip()
        password = request.POST.get("passwordInput", "")
        next_url = request.POST.get("next") or request.GET.get("next")
        print(username)
        
        user = authenticate(username=username, password=password)
        print("Authenticated user:", user)

        if user is not None and user.is_active:
            login(request, user)
            request.session["show_login_toast"] = True
            remember_me = request.POST.get("remember")
            if remember_me:
            	request.session.set_expiry(64800)
           

            
            return safe_redirect(request, next_url)
        return render (request,"accounts/login.html",{"show_toast": "Invalid username or password"})
    # return register(request)
    return render (request,"accounts/login.html",{"show_logout_toast":show_logout_toast})
    # anytime you call /logout page it opens accounts/login.html ,which in turn calls /logout page and dashboard/login.html page
    # is called automatically 


def logout_view(request):

   logout(request);
   request.session["show_logout_toast"] = "Successfully Logged out"
   # show_logout_toast = request.session.pop("show_logout_toast",False);
   # return render(request,"accounts/login.html",{"show_logout_toast":show_logout_toast})
   return redirect("accounts:login")