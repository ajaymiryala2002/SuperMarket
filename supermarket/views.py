from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def home_page(request):
    return render(request,'frontend/homepage.html')

def Register(request):
    message=""
    if request.metod=='POST':
        name=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        con_password=request.POST.get('conpassword')
        if password==con_password:
            try:
                user=User.objects.create_user(name,email,password)
                message='new user created successfully'
                return render('home')

            except IndentationError:
                message='user already created'
        else:
            message='Password incorrect'
    context={
        'message':message
    }
    return render(request,'frontend/firstREGISTER.html',context)


        




























def signUpUser(request):

    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email_id')
        p1 = request.POST.get('password')
        p2 = request.POST.get('confirm_password')

        if p1 == p2:
            try:
                user = User.objects.create_user(username,email,p1)
                user.save()
                message = 'User created successfully'
            except IndentationError:
                message = 'User already exists'
        else:
            message = 'Passwords do not match'

    context = {
        'message': message
    }

    return render(request, 'frontend/register.html', context)

def home1(request):
    return render(request,'frontend/first.html')

def productdetails(request):
    return render(request,'frontend/Pdetails.html')

