import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from .models import UserProfile

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import User


#from student_management_app.EmailBackEnd import EmailBackEnd

from django.shortcuts import render

# Create your views here.
def loginpage(request):
    return render(request,"login.html")

def registerpage(request):
    return render(request,"register.html")  




def user_register(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user=User.objects.create(username=username, password=password)

        user.set_password(password)
        user.save()
        return redirect('/register/')
    return render(request, "register.html")

    
def user_login(request):
    if request.method=='POST':
        username=request.POST.get['username']
        password=request.POST.get['password']
        user=authenticate(request,username=username,password=password)
        return redirect('/login/')
    return render(request,'student_management_app/login.html')