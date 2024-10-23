from django.urls import path, include
from socials import views


urlpatterns = [
    path('', views.homePage, name = "home"),
    path('app/', views.appPage, name = "app"),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('signup/', views.signUp, name = "signup"),
    path('facebook-logout/', views.facebook_logout_view, name='facebook_logout'),
    # path('accounts/facebook/callback/', views.facebook_callback_view, name='facebook_callback'),
]