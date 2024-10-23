from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import signupForm
from decouple import config
from allauth.socialaccount.models import SocialAccount, SocialToken
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

from django.conf import settings


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


def social_account_view(request): 
    accounts = SocialAccount.objects.filter(user=request.user)
    for account in accounts:
        print(account.extra_data)  # Check what data is available
    return render(request, "app.html", {'accounts': accounts})


def facebook_logout_view(request):

    # Get the user's Facebook access token
    try:
        social_token = SocialToken.objects.get(account__user=request.user, account__provider='facebook')
        access_token = social_token.token
    except SocialToken.DoesNotExist:
        access_token = None

    if access_token:
        # Facebook logout URL
        facebook_logout_url = (
            f"https://www.facebook.com/logout.php?"
            f"next={settings.FACEBOOK_LOGOUT_REDIRECT_URL}&access_token={access_token}"
        )
        return redirect(facebook_logout_url)
    
    # If no access token, redirect to home
    return redirect(settings.FACEBOOK_LOGOUT_REDIRECT_URL)


# def facebook_callback_view(request):
#     """Handle Facebook login callback."""
#     if request.user.is_authenticated:
#         # Check if the Facebook account is connected
#         try:
#             social_account = SocialAccount.objects.get(user=request.user, provider='facebook')
#             social_token = SocialToken.objects.get(account=social_account)

#             # Extract token and user details
#             token = social_token.token
#             uid = social_account.uid

#             # Redirect to the dashboard with token and UID
#             return render(request, 'app.html', {'token': token, 'uid': uid})

#         except SocialAccount.DoesNotExist:
#             # If Facebook account isn't connected, redirect to connect page
#             return redirect('account_login')

#     # If not authenticated, redirect to login
#     return redirect('account_login')
