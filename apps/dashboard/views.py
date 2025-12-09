from django.shortcuts import render,redirect
from django.http import HttpResponse;

def login_redirect(request):
	return render(request,"dashboard/exit.html");
def home_redirect(request):
	print("lol2")
	return redirect("login_page");
def main_redirect(request):
	print("lol")	
	return redirect("login_page");



# Create your views here.
