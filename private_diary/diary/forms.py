from django import forms

# Pythonクラスで入力フォールのデータを定義している
# MVCモデルのM(odel)を表している
class InquiryFrom (forms.Form):
    # フィールド変数が入力項目
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)
