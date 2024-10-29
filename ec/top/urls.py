# topアプリのURLマッピング処理

from django.urls import path

# このファイルと同じフォルダ内の views.py を参照する
from . import views

app_name = 'top'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
]
