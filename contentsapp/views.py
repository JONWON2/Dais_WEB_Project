from unicodedata import category
from django.shortcuts import render
from django.test import RequestFactory
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy


# Create your views here.
def intro_page(request):
    return render(request, 'contentsapp/lab_intro.html') 

def meetup_page(request):
    year = request.GET.get('year')
    request.session["year"] = str(year)
    return render(request, 'contentsapp/lab_meetup.html',{"year": str(year)})


def proud_page(request):
    year = request.GET.get('year')
    return render(request, 'contentsapp/lab_proud.html',{"year": str(year)}) 

def study_page(request):
    category = request.GET.get('category')

    return render(request, 'contentsapp/lab_study.html',{'category':category}) 

def notice_page(request):
    return render(request, 'contentsapp/lab_notice.html') 



