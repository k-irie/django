from django.shortcuts import render
# from django.views import generic
from django.views.generic import TemplateView


# Create your views here.
# ここにクラスを登録することによりアプリ内の画面を登録する

#   IndexViewクラスはindex.htmlを元にページを構成する
class IndexView(TemplateView) :
    template_name = "index.html"
