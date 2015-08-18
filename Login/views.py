# -*- coding=utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from Login.models import Users
from django import forms
import ctypes
import os

# Create your views here.

#定义表单模型
class UserForm(forms.Form):
    user_name = forms.CharField(label='用户名:', max_length=50)
    pass_word = forms.CharField(label='密  码:', max_length=50, widget=forms.PasswordInput())

def GenPicture():
    path = os.getcwd()
    libLoadEcg = ctypes.cdll.LoadLibrary(path + '/libcn100_compress.so')
    lpBuf = [[] for i in range(12)]
    libLoadEcg.ReadReviewFile(path+'/20150519112355024161291461318950.003', ctypes.c_int16_p(lpBuf))


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
                GenPicture();
                return render_to_response('success.html',{'user_name':user_name})
            else:
                return HttpResponseRedirect('/Login/')

    else:
        uf = UserForm()

    return render_to_response('Login.html', {'uf':uf})