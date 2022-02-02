from unicodedata import category
from django.shortcuts import render
from django.test import RequestFactory
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views import View  

# Create your views here.
def intro_page(request):
    return render(request, 'contentsapp/lab_intro.html') 

## 초기에 화면 View를 위해 사용한 함수.
# def meetup_page(request):
#     year = request.GET.get('year')
#     request.session["year"] = str(year)
#     return render(request, 'contentsapp/lab_meetup.html',{"year": str(year)})
# def proud_page(request):
#     year = request.GET.get('year')
#     return render(request, 'contentsapp/lab_proud.html',{"year": str(year)}) 
# def study_page(request):
#     category = request.GET.get('category')
#     return render(request, 'contentsapp/lab_study.html',{'category':category}) 
# def notice_page(request):
#     return render(request, 'contentsapp/lab_notice.html') 

## 기능을 추가하기위해 GET과 POST에 대해 구분 지은 클래스 View
class meetup_page(View):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year')
        request.session["year"] = str(year)
        return render(request, 'contentsapp/lab_meetup.html',{"year": str(year)})
    def post(self, request, *args, **kwargs):
        year = request.GET.get('year')[:-1]
        request.session["year"] = str(year)
        return HttpResponseRedirect(reverse('contentsapp:meetup_write'))

        # return render(request, 'contentsapp/write_meetup.html',{"year": str(year)})
class meetup_write_page(View):
    def get(self, request, *args, **kwargs):
        year = request.session["year"]
        print("GET으로 받음?")
        return render(request, 'contentsapp/write_meetup.html')

    def post(self, request, *args, **kwargs):
        print("POST으로 받음?")
        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            year = request.session["year"]
            return render(request, 'contentsapp/lab_meetup.html',{"year": str(year)+"/"})
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            year = request.session["year"]
            return render(request, 'contentsapp/lab_meetup.html',{"year": str(year)+"/"})
        return  HttpResponseRedirect(reverse('app:main'))

#############################################################
class proud_page(View):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year')
        request.session["year"] = str(year)
        return render(request, 'contentsapp/lab_proud.html',{"year": str(year)})
    def post(self, request, *args, **kwargs):
        year = request.GET.get('year')[:-1]
        request.session["year"] = str(year)
        return HttpResponseRedirect(reverse('contentsapp:proud_write'))

class proud_write_page(View):
    def get(self, request, *args, **kwargs):
        year = request.session["year"]
        print("GET으로 받음?")
        return render(request, 'contentsapp/write_proud.html')

    def post(self, request, *args, **kwargs):
        print("POST으로 받음?")
        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            year = request.session["year"]
            return render(request, 'contentsapp/lab_proud.html',{"year": str(year)+"/"}) 
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            year = request.session["year"]
            return render(request, 'contentsapp/lab_proud.html',{"year": str(year)+"/"}) 
        return  HttpResponseRedirect(reverse('app:main'))


#############################################################
class study_page(View):
    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')
        request.session["category"] = category
        return render(request, 'contentsapp/lab_study.html',{"category": str(category)})

    def post(self, request, *args, **kwargs):
        category = request.GET.get('category')
        request.session["category"] = category
        return HttpResponseRedirect(reverse('contentsapp:study_write'))

class study_write_page(View):
    def get(self, request, *args, **kwargs):
        print("GET으로 받음?")
        return render(request, 'contentsapp/write_study.html')

    def post(self, request, *args, **kwargs):
        print("POST으로 받음?")
        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            category = request.session["category"]
            return render(request, 'contentsapp/lab_study.html',{"category": category}) 
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            category = request.session["category"]
            return render(request, 'contentsapp/lab_study.html',{"category": category}) 

        return  HttpResponseRedirect(reverse('app:main'))

#############################################################


class notice_page(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contentsapp/lab_notice.html')

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('contentsapp:notice_write'))

class notice_write_page(View):
    def get(self, request, *args, **kwargs):
        print("GET으로 받음?")
        return render(request, 'contentsapp/write_notice.html')

    def post(self, request, *args, **kwargs):
        print("POST으로 받음?")
        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            return render(request, 'contentsapp/lab_notice.html') 
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            return render(request, 'contentsapp/lab_notice.html') 
        return  HttpResponseRedirect(reverse('app:main'))



