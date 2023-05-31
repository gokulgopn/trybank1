from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def Homepage(request):
    return render(request, 'home.html', {})

def Registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        new_user = User.objects.create_user(username, password, password2)
        new_user.save()
        return redirect('login')

    return render(request, 'register.html', {})

def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')