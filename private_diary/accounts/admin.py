from django.contrib import admin

# Register your models here.

from .models import CustumUser

# 管理画面にユーザ登録アプリを登録する
admin.site.register(CustumUser)
