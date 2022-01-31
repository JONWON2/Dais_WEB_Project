from django.contrib import admin
from django.urls import path
from contentsapp import views
from django.contrib.auth import views as auth_views

app_name = 'contentsapp'

urlpatterns = [
    path('intro/', views.intro_page,name='intro'),
]
