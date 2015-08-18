# -*- coding=utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from Login.models import Users
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

#定义表单模型
class UserForm(forms.Form):
    user_name = forms.CharField(label='用户名:', max_length=50)
    pass_word = forms.CharField(label='密  码:', max_length=50, widget=forms.PasswordInput())



#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户名和密码
            user_name = uf.cleaned_data['user_name']
            pass_word = uf.cleaned_data['pass_word']

            #表单数据和数据库比较
            user = Users.objects.filter(user_name__exact=user_name, user_pwd__exact=pass_word)

            if user:
                # user_save = User.objects.create_user(username=user_name,password=pass_word,email='xx@xx.xx')
                # user_save.save
                # user_login = auth.authenticate(username=user_name, password=pass_word)
                auth.login(request, user)
                return HttpResponseRedirect('/Show/')
                # return render_to_response('success.html',{'user_name':user_name})
            else:
                return HttpResponseRedirect('/Login/')

    else:
        uf = UserForm()

    return render_to_response('Login.html', {'uf':uf})

