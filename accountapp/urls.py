from django.contrib import admin
from django.urls import path
from accountapp import views
from django.contrib.auth import views as auth_views

app_name = 'accountapp'

urlpatterns = [
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('signout/', views.signout,name='signout'),
]
