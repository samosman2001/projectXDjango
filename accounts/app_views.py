from django.shortcuts import render
from django.http import JsonResponse
import json,secrets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.core.mail import send_mail
from django.core.cache import cache 
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm

# def app_login (request):
#     if request.method == "POST":
#     	email = request.POST.get("email").strip()
#     	password = request.POST.get("password")
#     	user = authenticate(username=email, password=password)
#     	if user is not None and user.is_active:
#             login(request, user)
#             request.session["show_login_toast"] = "Successfully Logged In"
#             remember_me = request.POST.get("remember")
#             if remember_me:
#             	request.session.set_expiry(64800)
#             	return render(request,"mainApp.html")
#             return render (request,"appLogin.html",{"show_toast": "Invalid username or password"})       
#     return render (request,"appLogin.html")
# @login_required
# def dashboard_api(request):
# 	return render(request,"mainApp.html")

# skipping CSRF = Cross-Site Request Forgery for mobile apps 
User = get_user_model()

OTP_TTL_SECONDS = 5 * 60
OTP_COOLDOWN = 60
OTP_MAX_ATTEMPTS = 5

def __norm_email__(email : str)->str :
    if not "@" or not "." in email:
        return ""
    return (email or "").strip().lower()

def __otp_key__(email:str)->str :
    return f"otpkey : {email}"
def __otp_meta__(email:str)->str:
    return f"otp meta : {email}"

@require_POST
@csrf_exempt
def request_email_otp(request):
    """POST JSON {"email" : "user@example.com"}
           
    """
    try : 
        data = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"success":False,"error":"Invalid JSON"},status = 400)
    email = __norm_email__(data.get("email"))
    if not email:
        return JsonResponse({"success": False,"error":"Invalid Email Address"},status = 400 )
    try:
        #email__iexact stands for field__lookup
        #field should be the field we are looking for 
        #iexact is "case insensitive exact" 
        user = User.objects.get(email__iexact = email)
    except User.DoesNotExist:
        user,created  = User.objects.get_or_create(
            username = email,
             defaults={"email": email} )
        # return JsonResponse({"success":False,"error":"No Account for this email "},status = 404)
    meta = cache.get(__otp_meta__(email)) or {}
    last_sent_ts = meta.get("last_sent_ts")
    if last_sent_ts:
        seconds_ago = timezone.now().timestamp() - last_sent_ts
        if seconds_ago < OTP_COOLDOWN:
            return JsonResponse({"success":False,"error":f"Wait {(OTP_COOLDOWN - seconds_ago):.0f} seconds " },status = 429)
    otp = f"{secrets.randbelow(1_000_000):06d}" #random 0..999999
    cache.set(__otp_key__(email),otp,timeout = OTP_TTL_SECONDS)
    cache.set(__otp_meta__(email),{"attempts":0,"last_sent_ts":timezone.now().timestamp()}
    ,timeout =OTP_TTL_SECONDS)

    send_mail(subject = "Enter your email here",
        message = f"Your OTP code is {otp}\n \n it expires in 5 mins",
        from_email = None,
        recipient_list = [email],
        fail_silently = False,)
    return JsonResponse({"success" : True,"message" : "OTP sent"})
 

@require_POST
@csrf_exempt
def verify_email_otp(request):
    """
    POST JSON: 
    """
    try:
        data = json.loads(request.body.decode("utf-8")) or {}
    except json.JSONDecodeError:
        return JsonResponse({"success" : False,"error":"Invalid Json"},status = 404)
    email = __norm_email__(data.get("email"))
    otp_input = data.get("otp") or ""

    if not email or not otp_input:
        return JsonResponse({"success":False,"error":"No email and Otp key found"},status = 400)
    meta = cache.get(__otp_meta__(email)) 
    otp = cache.get(__otp_key__(email))
    
    if not otp:
        return JsonResponse({"success" : False,"error":"OTP expired"},status = 400)
    meta["attempts"] = int(meta.get("attempts",0)) + 1
    cache.set(__otp_meta__(email),meta,timeout = OTP_TTL_SECONDS)
    if meta["attempts"] > OTP_MAX_ATTEMPTS:
        cache.delete(__otp_key__(email))
        cache.delete(__otp_meta__(email))
        return JsonResponse({"success": False,"error":"Too Many Attempts ,request new OTP"},status = 400)
    
    if otp_input!= otp:
        return JsonResponse({"success" : False,"error" : "Invalid OTP"},status = 401 )

    try :

        user = User.objects.get(email__iexact = email)
    except User.DoesNotExist:
        return JsonrResponse({"success" : False,"error":"Such a user does not exist"},status = 404)
    login(request,user,backend="django.contrib.auth.backends.ModelBackend")
    cache.delete(__otp_key__(email))
    cache.delete(__otp_meta__(email))
    return JsonResponse({"success": True,"message" : "Successfully Logged in "})




@csrf_exempt
def app_login(request):
    if request.method !="POST":
        return JsonResponse({
            "success":False,
            "error" : "Post method Required" 
            },status = 405)

    username = request.POST.get("username")
    email = request.POST.get("loginEmail")
    password = request.POST.get("loginPassword")
    remember_me = request.POST.get("remember")
    
    user = authenticate(username=email,password = password)

    if not email or not password:
        return JsonResponse({
            "success":False,
            "error":"Fill up credentials"
            })
    if user is None:
        return JsonResponse({
            "success":False,
            "error" :"Invalid User "
            },status = 401)



    if  not user.is_active:

        return JsonResponse({
            "success":False,
            "error":"User Account disabled"
            },403)
    login(request,user)
    if remember_me:
        request.session.set_expiry(60 * 60 * 18)
    else:
        request.session.set_expiry(0)
    return JsonResponse({
        "success" :True,
     "user":{
     "id" :user.id,
     "email":user.email,
     "username" : user.username,
     }

        })

def app_logout(request):
    logout(request)
    return JsonResponse({
        "success":True,
        "data":"Successfully Logged out"
        })
