from django.db import models

# ログインユーザ情報
from accounts.models import CustumUser

# Create your models here.


# 日記投稿用モデル
class Diary(models.Model):
    # データベースへのフィールド定義
    #   SQLのUPDATE、INSERT INTOでの型定義
    # 日記を投稿している人の情報
    user = models.ForeignKey(
        CustumUser,
        verbose_name='ユーザー',
        on_delete=models.PROTECT)
    # 以下 1件分の日記内容
    title = models.CharField(verbose_name='タイトル',max_length=40)
    content = models.TextField(verbose_name='本文',blank=True,null=True)
    photo1 = models.ImageField(verbose_name='写真1',blank=True,null=True)
    photo2 = models.ImageField(verbose_name='写真2',blank=True,null=True)
    photo3 = models.ImageField(verbose_name='写真3',blank=True,null=True)
    # 自動的に処理日時をセットする
    create_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)


    class Meta:
        verbose_name_plural = 'Diary'

    // オブジェクトを文字列として表す場合の文字列パターン
    def __str__(self):
        return self.title
    