# settings_dev.py
# 開発環境用の設定を行う

# settings_common.py から全ての設定を読み込む
from .settings_common import *


# # 開発環境なのでメール内容をSMTPサーバへ送信せず、ターミナル上に出力する
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
