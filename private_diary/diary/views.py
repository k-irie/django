from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView

from .forms import InquiryForm

# お問い合わせ送信内容をログに残す
import logging
logger = logging.getLogger(__name__)

# 'アプリ名:url名'からURLを取り出す
from django.urls import reverse_lazy

# Create your views here.
# ここにクラスを登録することによりアプリ内の画面を登録する

#   IndexViewクラスはindex.htmlを元にページを構成する
class IndexView(TemplateView) :
    template_name = 'index.html'

# お問い合わせページ
class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    # フォーム画面を表示するだけならここまで

    # 送信に成功した後に表示するURL
    success_url = reverse_lazy('diary:index')

    # メソッドのオーバーライド
    #   フォームに正しい値が入力され送信された時の処理
    def form_valid(self, form) :
        # メールを送信する
        form.send_mail()
        # 送信したことをログに残す
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))

        return super().form_valid(form)
