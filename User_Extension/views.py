from django.http import HttpResponse
from django.shortcuts import redirect,reverse,render
from .models import *
# from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



def index(request):
    username='zhiliao2@qq.com'
    password='222222'
    user=authenticate(request,username=username,password=password)
    if user:
        print('用户登录正确',username)
    else:
        print('用户登录错误')
    return HttpResponse("首页")
