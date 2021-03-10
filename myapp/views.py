from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html', {})


def registration(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        passw1 = request.POST.get('password')
        passw2 = request.POST.get('password1')
        dob = request.POST.get('dob')
        img = request.FILES.get('img')
        if passw1 == passw2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'The Email is already in use')
                return redirect('user:signup')
            elif img:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=email,
                                                password=passw1, dob=dob, img=img)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return redirect('myapp:login')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=email,
                                                password=passw1, dob=dob)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return redirect('myapp:login')
        else:
            messages.info(request, 'The passwords are not matching')
            return redirect('myapp:login')
    return render(request, 'registration.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(request.user)
            print(request.auth)
            return redirect('myapp:index')
        else:
            messages.info(request, 'Invalid Login')
            return redirect('myapp:login')  
    return render(request, 'login.html', {})


def logout(request):
    auth.logout(request)
    messages.info(request, 'Successfull Logout')
    return render(request, 'login.html', {})