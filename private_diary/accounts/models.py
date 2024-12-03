from django.contrib.auth.models import AbstractUser

# Create your models here.
# AbstructUserクラスを継承したCustumUserクラス
class CustumUser(AbstractUser) :
    """ 拡張ユーザモデル """

    class Meta:
        verbose_name_plural = 'CustumUser'
