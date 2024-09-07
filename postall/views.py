from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages

def homePage(request):
    return render(request, "home.html")

def loginPage(request):
    return render(request, "login.html")

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