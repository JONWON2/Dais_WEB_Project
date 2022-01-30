from email.policy import default
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import  HttpResponseRedirect
from django.urls import reverse
from collections import defaultdict
from .models import User_info

def signin(request):
    if request.method =='POST':
        username = request.POST.get('user_id')
        password = request.POST.get('password')
        try:
            user = User_info.objects.get(user_id = username)
            if password != user.user_pw:
                messages.info(request, '비밀번호를 확인해주세요.')
                return HttpResponseRedirect(reverse('accountapp:signin'))   
            else:
                username = user.user_id
        except User_info.DoesNotExist as e:
                messages.info(request, '확인되지 않는 아이디입니다.')
                return HttpResponseRedirect(reverse('accountapp:signin'))   
        else:
            request.session['user'] = username
        return HttpResponseRedirect(reverse('app:main'))    
    else:
        return render(request,'accountapp/signin.html')

def signup(request):
    if request.method =='POST':
        user_name = request.POST.get('userName')
        user_id = request.POST.get('userId')
        user_pw =  request.POST.get('password1')
        user_pw_check =request.POST.get('password2')
        user_phone = "010"+request.POST.get('ph2')+request.POST.get('ph3')
        user_email = request.POST.get('userEmail')
        if user_pw_check != user_pw:
            messages.info(request, '비밀번호가 일치하지 않습니다.')
            return HttpResponseRedirect(reverse('accountapp:signup'))   
        try:
            user = User_info.objects.get(user_id = user_id)
            messages.info(request, '사용중인 아이디입니다.')
            return HttpResponseRedirect(reverse('accountapp:signup'))
        except User_info.DoesNotExist as e:
            print("잉??")
            m = User_info(user_id=user_id, user_pw=user_pw, user_name=user_name,user_email=user_email,user_phone=user_phone)
            m.save()
            return HttpResponseRedirect(reverse('app:main')) 
    else:
        return render(request,'accountapp/signup.html')

def signout(request):
    del request.session['user']
    return redirect('/app/main/')