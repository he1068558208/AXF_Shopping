import random
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse


from user.models import UserModel, UserTicketModel
from utils.functions import get_ticket


def register(request):
    if request.method == 'GET':

        return render(request,'user/user_register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        if not all([username,password,email,icon]):
            msg = '注册消息不能为空'
            return render(request,'user/user_register.html',{'msg':msg})

        UserModel.objects.create(username=username,password=make_password(password),email=email,icon=icon)
        return HttpResponseRedirect('/user/login')

def login(request):
    if request.method == 'GET':
        return render(request,'user/user_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user = UserModel.objects.filter(username=username).first()
        if user:
            if check_password(passwd,user.password):
                ticket = get_ticket()
                response = HttpResponseRedirect('/axf/mine')
                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket',ticket,expires=out_time)

                UserTicketModel.objects.create(user=user,
                                               out_time=out_time,
                                               ticket=ticket)
                return response
            else:
                msg = '密码错误'
                return render(request,'user/user_login.html',{'msg':msg})
        else:
            msg = '用户不存在'
            return render(request,'user/user_login.html',{'msg':msg})

def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect('/user/login')
        response.delete_cookie('ticket')

        return response