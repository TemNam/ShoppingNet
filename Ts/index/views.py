from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *

# Create your views here.

@login_required
def index_(request):
    return render(request, 'index.html')

def login_(request): #登录用户
    if request.method == 'GET':
        url = request.META.get('HTTP_REFERER', '/')
        request.session['url'] = url
        return render(request, 'login.html')
    else:
        name = request.POST['username']
        upwd = request.POST['upwd']
        user = auth.authenticate(username=name, password=upwd)
        print(user, type(user), user.username)
        if user:
            auth.login(request, user)
            url = request.session['url']
            print(url)
            if url == 'http://127.0.0.1:8000/register/':
                return redirect('/')
            return redirect(url)
        else:
            params = {'msg': '登录失败'}
            return render(request, 'login.html', locals())

def register_(request): #注册用户
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        upwd1 = request.POST['upwd1']
        upwd2 = request.POST['upwd2']
        if upwd1 == upwd2:
            if not UserInfo.objects.filter(username=username):
                user = UserInfo.objects.create_user(username=username, password=upwd1)
                auth.login(request, user)
            return redirect('/')
        else:
            params = {'msg': '注册失败'}
            return render(request, 'register.html', locals())

def logout_(request): #退出账户
    auth.logout(request)
    return redirect('/login/')

def selfinfo_(request, id):
    print(id)
    return HttpResponse('个人主页')

def queryName_(request): #ajax请求,判断用户名是否存在
    if request.method == 'POST':
        uname = request.POST['username']
        user = UserInfo.objects.filter(username=uname)
        if uname != '':
            if not user:
                return HttpResponse('ok')
            else:
                return HttpResponse('用户已存在')
        else:
            return HttpResponse('用户名不能为空')