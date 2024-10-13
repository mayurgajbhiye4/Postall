from django.urls import path, include
from socials import views


urlpatterns = [
    path('', views.homePage, name = "home"),
    path('app/', views.appPage, name = "app"),
    path('', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('signup/', views.signUp, name = "signup"),
]