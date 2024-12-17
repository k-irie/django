"""
URL configuration for private_diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path
# 2024/10/01 追加 → プロジェクト内のアプリを参照する
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static

# 設定ファイルの読み込み
from . import settings, settings_dev

urlpatterns = [
    path("admin/", admin.site.urls),
    # diaryアプリへのルートを定義する
    # 第一引数はURI上のアプリのフォルダ示す
    #   '' はトップフォルダとなる
    path("", include("diary.urls")),
    path("accounts/", include("allauth.urls")),
]

# メディア配信用設定
#   /media/へアクセスした時に開くフォルダを関連付ける
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
