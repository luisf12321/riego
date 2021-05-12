
from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


@login_required
def usuarios(request):
    return  render(request, 'user/feed.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        print(email, password)
        print('*'*10)
        userlogin = authenticate(request, username=email, password=password)
        print(userlogin)
        if userlogin:
            login(request, userlogin)
            return redirect("usuario")
        else:
            return render(request, "user/login.html",{"error":"invalido email 0 password"})

    return render(request, "user/login.html")


def registro(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print(firstname,lastname,email,username,password)
        try:
            user_new = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
            return redirect("login")
        except:
            return render(request, "user/registro.html",{"message":"el username ya existe"})
    return render(request, "user/registro.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def perfil(request):
    return render(request, "user/perfil.html")

