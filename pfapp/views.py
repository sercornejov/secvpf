from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from pfapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
import json
import datetime

def index_view(request):
    response_data = {
        'h_content':'A simple way to set-up your portfolio online',
        'para_home':'To create your PORTFOLIO, is necessary to register a new user. You can create a new user by clicking on "Register" button, or if you are a registered used, please login into your account',
    }
    return render(request,'main/index.html', response_data)

def home_view(request):
    current_user = request.user
    print(current_user.id)
    print(current_user.username)
    
    actualuser=Geninfo.objects.filter(user=current_user.id).values()
    
    print(actualuser)
    
    
    
    #firstname=actualuser.firstname
    
    #print(firstname)
    
    return render(request, 'main/home.html', {'username': current_user.username, 'userid': current_user.id, 'actualuser': actualuser})

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register_user.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'main/login_user.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def editUser_view(request):
    current_user = request.user
    print(current_user.id)
    print(current_user.username)

    return render(request,'usus/editUser.html', {'username': current_user.username, 'userid': current_user.id})