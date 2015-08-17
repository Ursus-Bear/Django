# -*- coding=utf-8 -*-
from django.db import models
from django.contrib import admin

# Create your models here.
class Users(models.Model):
    user_num = models.CharField(max_length=50, primary_key=True)
    user_name = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_role = models.IntegerField(help_text='1:采集医生;2:诊断医生')
    user_hospital = models.CharField(max_length=50)


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_num', 'user_name', 'user_pwd', 'user_role', 'user_hospital')

admin.site.register(Users, UserAdmin)