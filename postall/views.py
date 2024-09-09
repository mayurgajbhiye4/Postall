from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def homePage(request):
    return render(request, "home.html")

@login_required(login_url="/login/")
def appPage(request):
    return render(request, "app.html")

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')

        user = authenticate(username =username, password=password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect('/login/') 
        else:
            login(request, user)
            return redirect('/app/')
        
    return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect ('/login/')


def signUp(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/signup/')

        user = User.objects.create(
              first_name = first_name,
              last_name = last_name,
              username = username,    
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect('/signup/')

    return render(request, "signup.html")