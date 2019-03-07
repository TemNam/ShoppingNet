from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *

# Create your views here.

@login_required
def index_(request):
    return render(request, 'index.html')

def login_(request):
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
            return redirect(url)
        else:
            params = {'msg': '登录失败'}
            return render(request, 'login.html', locals())

def register_(request):
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
            params = {'msg': '登录失败'}
            return render(request, 'register.html', locals())


def logout_(request):
    auth.logout(request)
    return redirect('/login/')