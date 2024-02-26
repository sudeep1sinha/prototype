import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from .models import UserProfile
from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User


# from student_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/iflogin/')
        else:
            print('invalid credentials')
    else:
        return render(request, "login.html")


def registerpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username, password=password)

        user.save()
        return redirect('/login/')
    else:
        return render(request, "register.html")


def iflogin(request):
    return render(request, "iflogin.html")
