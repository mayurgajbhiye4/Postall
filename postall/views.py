from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import signupForm

def homePage(request):
    return render(request, "home.html")

@login_required(login_url="/login/")
def appPage(request):
    return render(request, "app.html")

def signUp(request):
    if request.method == "POST":    
        form = signupForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)   
            user.save()
            messages.info(request, "Account created successfully")
            return redirect('/signup/')
    else:
        form = signupForm()

    return render(request, "registration/signup.html", {'form':form})



