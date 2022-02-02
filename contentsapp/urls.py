from django.contrib import admin
from django.urls import path
from contentsapp import views
from django.contrib.auth import views as auth_views

app_name = 'contentsapp'

urlpatterns = [
    path('intro/', views.intro_page,name='intro'),
    path('meetup/', views.meetup_page,name='meetup'),
    path('proud/', views.proud_page,name='proud'),
    path('study/', views.study_page,name='study'),
    path('notice/', views.notice_page,name='notice'),
]
