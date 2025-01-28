from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import InquiryForm

# お問い合わせ送信内容をログに残す
import logging
logger = logging.getLogger(__name__)

# 'アプリ名:url名'からURLを取り出す

# ページ間でメッセージを送る機能

# Create your views here.
# ここにクラスを登録することによりアプリ内の画面を登録する

#   IndexViewクラスはindex.htmlを元にページを構成する


class IndexView(TemplateView):
    template_name = 'index.html'

# お問い合わせページ


class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    # フォーム画面を表示するだけならここまで

    # 送信に成功した後に表示するURL
    success_url = reverse_lazy('diary:index')
    # success_url = reverse_lazy('diary:inquiry')

    # メソッドのオーバーライド
    #   フォームに正しい値が入力され送信された時の処理
    def form_valid(self, form):
        # メールを送信する
        form.send_mail()
        # メールを送信したメッセージを次のページへ送る
        messages.success(self.request, 'メッセージを送信しました')
        messages.success(self.request, 'CCでメールを同報しています')
        messages.success(self.request, 'ご確認下さいませ')
        # 送信したことをログに残す
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))

        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
from django.core.paginator import Page

# 日記一覧
#   ログインが必要で尚且つ一覧表示するViewを継承する
class DiaryListView(LoginRequiredMixin,generic.ListView) :
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    # 問い合わせ条件を設定する
    # ※今回は全行ではなくログインしている人の日記のみが対象となる
    def get_queryset(self):
        # Diaryテーブルから条件に当てはまる行を抽出する
        #   ログインユーザの日記のみを抽出する
        #   登録日付の降順に並び替える
        diaries = Diary.objects.filter(user=self.request.user).order_by('-create_at')
        return diaries
        # return super().get_queryset()

# 日記を1件表示するビュー
#   DetailViewではpk変数で主キーを受け取る
class DiaryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html'

# 日記を作成するビュー
from .forms import DiaryCreateForm
class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class =  DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self,form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()

        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'日記を作成に失敗しました。')
        return super().form_invalid(form)