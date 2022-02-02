from django.contrib import admin
from django.urls import path
from contentsapp import views
from django.contrib.auth import views as auth_views

app_name = 'contentsapp'

urlpatterns = [
    path('intro/', views.intro_page,name='intro'),
    path('meetup/', views.meetup_page.as_view(),name='meetup'),
    path('meetup/write/', views.meetup_write_page.as_view(),name='meetup_write'),
    
    path('proud/', views.proud_page.as_view(),name='proud'),
    path('proud/write/', views.proud_write_page.as_view(),name='proud_write'),

    path('study/', views.study_page.as_view(),name='study'),
    path('study/write/', views.study_write_page.as_view(),name='study_write'),

    path('notice/', views.notice_page.as_view(),name='study'),
    path('notice/write/', views.notice_write_page.as_view(),name='notice_write'),

]
