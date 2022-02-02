from django.shortcuts import render
from django.test import RequestFactory
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views import View  
from .models import *
from accountapp.models import *
from django.contrib import messages
import datetime,os

# Create your views here.
def intro_page(request):
    return render(request, 'contentsapp/lab_intro.html') 

#--------------------------------------------------------------
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


#--------------------------------------------------------------
## 기능을 추가하기위해 GET과 POST에 대해 구분 지은 클래스 View
class meetup_page(View):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year')
        request.session["year"] = str(year)

        DB_M =MeetupDB.objects.filter(year=year[:-1])
        return render(request, 'contentsapp/lab_meetup.html',{"DB": DB_M})

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
        # 입력한 내용 가져오기 비어있는 내용이면, False로!! 
        title = request.POST.get('title',False)
        contents = request.POST.get('contents',False)
        upload_file = request.FILES.get('file',False)
        year = request.POST.get('year',False)

        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            year = request.session["year"]
            return render(request, 'contentsapp/lab_meetup.html',{"year": str(year)+"/"})
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            # 한개라도 False가 아니면 DB에 저장 하나로도 False이면 다시 입력해달라고 요청
            if title and contents and upload_file and year:
                DB_M =MeetupDB()
                number = str(len(MeetupDB.objects.all())+1)

                DB_M.user_id = request.session['user']
                DB_M.title = title
                DB_M.contents = contents
                DB_M.meet_regi_date = datetime.datetime.now().strftime ("%Y-%m-%d")
                DB_M.year = year


                # 파일을 local 환경에 저장하는 코드
                # 파일 이름이 중복이 되지 않게 저장하기
                upload_file_name = "".join(upload_file.name.split(" "))
                upload_file_name = upload_file_name.replace("(","")
                upload_file_name = upload_file_name.replace(")","")
                
                file_name = request.session['user']+ number+"_"+ upload_file_name
                path = os.path.join("media/img/meetup/",file_name)
                with open(path, 'wb') as file:
                    file.write(upload_file.read())
                    for chunk in upload_file.chunks():
                        file.write(chunk)
                DB_M.meet_image_path =  "/"+path

                DB_M.save()  # DB에 저장완료.

                year = request.session["year"]
                return HttpResponseRedirect("/app/contentsapp/meetup/?year=2022/") 
            else:
                messages.info(request, '입력되지 않은 칸이 있습니다. 다 입력해주세요.')
                return HttpResponseRedirect(reverse('contentsapp:meetup_write')) 
        return  HttpResponseRedirect(reverse('app:main'))

#############################################################
class proud_page(View):
    def get(self, request, *args, **kwargs):
        year = request.GET.get('year',"2022/")
        request.session["year"] = str(year)

        DB_P =ProudDB.objects.filter(year=year[:-1])
        return render(request, 'contentsapp/lab_proud.html',{"DB": DB_P})

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
        title = request.POST.get('title',False)
        contents = request.POST.get('contents',False)
        upload_file = request.FILES.get('file',False)
        year = request.POST.get('year',False)

        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            year = request.session["year"]
            return render(request, 'contentsapp/lab_proud.html',{"year": str(year)+"/"}) 
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            if title and contents and upload_file and year:
                DB_P =ProudDB()
                number = str(len(ProudDB.objects.all())+1)
                DB_P.user_id = request.session['user']
                DB_P.title = title
                DB_P.contents = contents

                # 파일을 local 환경에 저장하는 코드
                # 파일 이름이 중복이 되지 않게 저장하기
                upload_file_name = "".join(upload_file.name.split(" "))
                upload_file_name = upload_file_name.replace("(","")
                upload_file_name = upload_file_name.replace(")","")
                
                file_name = request.session['user']+ number+"_"+ upload_file_name
                path = os.path.join("media/img/proud/",file_name)
                with open(path, 'wb') as file:
                    file.write(upload_file.read())
                    for chunk in upload_file.chunks():
                        file.write(chunk)
                DB_P.proud_image_path =  "/"+path

                DB_P.year = year
                DB_P.proud_regi_date = datetime.datetime.now().strftime ("%Y-%m-%d")
                DB_P.save()  # DB에 저장완료.
                year = request.session["year"]
                return HttpResponseRedirect("/app/contentsapp/proud/?year=2022/") 
            else:
                messages.info(request, '입력되지 않은 칸이 있습니다. 다 입력해주세요.')
                return HttpResponseRedirect(reverse('contentsapp:proud_write')) 

        return  HttpResponseRedirect(reverse('app:main'))


#############################################################
class study_page(View):
    def get(self, request, *args, **kwargs):
        category = request.GET.get('category',"전체")
        request.session["category"] = category
        if category[:-1] == "전체":
            print("전체")
            DB_S =StudyDB.objects.all()
        else:
            print("카테고리 : ",category)
            DB_S =StudyDB.objects.filter(category = category[:-1])
        print(len(DB_S))
        return render(request, 'contentsapp/lab_study.html', {"DB" : DB_S})

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
        title = request.POST.get('title',False)
        contents = request.POST.get('contents',False)
        category = request.POST.get('category',False)
        links = request.POST.get('links',False)

        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            category = request.session["category"]
            return render(request, 'contentsapp/lab_study.html',{"category": category}) 
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            if title and contents and links and category:
                DB_S =StudyDB()
                DB_S.user_id = request.session['user']
                DB_S.title = title
                DB_S.contents = contents
                DB_S.category = category
                DB_S.link_url = links
                DB_S.study_regi_date = datetime.datetime.now().strftime ("%Y-%m-%d")
                number = str(len(StudyDB.objects.all()) +1)
                DB_S.head_name = "heading" +number
                DB_S.id_name = "collapse" + number
                DB_S.head_id_name = "#collapse"+number
                DB_S.save()  # DB에 저장완료.
                return HttpResponseRedirect("/app/contentsapp/study/?category=전체/") 

            else:
                messages.info(request, '입력되지 않은 칸이 있습니다. 다 입력해주세요.')
                return HttpResponseRedirect(reverse('contentsapp:study_write')) 
        return  HttpResponseRedirect(reverse('app:main'))

#############################################################

class notice_page(View):
    def get(self, request, *args, **kwargs):
        DB_N =NoticeDB.objects.all()
        return render(request, 'contentsapp/lab_notice.html', {"DB" : DB_N,
            })

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('contentsapp:notice_write'))

class notice_write_page(View):
    def get(self, request, *args, **kwargs):
        print("GET으로 받음?")
        return render(request, 'contentsapp/write_notice.html')

    def post(self, request, *args, **kwargs):
        print("POST으로 받음?")
        title = request.POST.get('title',False)
        contents = request.POST.get('contents',False)
        # 이전 버튼을 눌렀을때
        if request.POST.get('before',False):
            return render(request, 'contentsapp/lab_notice.html') 
        # 완료 버튼을 눌렀을때
        if request.POST.get('finish',False):
            if title and contents:
                DB_N =NoticeDB()
                number = str(len(NoticeDB.objects.all()) +1)
                DB_N.user_id = request.session['user']
                DB_N.title = title
                DB_N.contents = contents
                DB_N.info_regi_date = datetime.datetime.now().strftime ("%Y-%m-%d")
                DB_N.head_name = "heading" +number
                DB_N.id_name = "collapse" + number
                DB_N.head_id_name = "#collapse"+number
                DB_N.save()  # DB에 저장완료.
                return HttpResponseRedirect(reverse('contentsapp:notice')) 
            else:
                messages.info(request, '입력되지 않은 칸이 있습니다. 다 입력해주세요.')
                return HttpResponseRedirect(reverse('contentsapp:notice_write')) 
        return  HttpResponseRedirect(reverse('app:main'))



