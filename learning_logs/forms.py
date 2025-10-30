# Topicモデルクラスの入力フォームクラス
from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    # どのModelクラスと紐づけるか
    class Meta:
        model = Topic  # このフォームが対応するモデル
        fields = ['text']  # フォームに表示するフィールド
        labels = {'text': ''}  # ラベルのカスタマイズ（空にして非表示）

class EntryForm(forms.ModelForm):
    # どのModelクラスと紐づけるか
    class Meta:
        model = Entry  # このフォームが対応するモデル
        fields = ['text']  # フォームに表示するフィールド
        labels = {'text': ''}  # ラベルのカスタマイズ（空にして非表示）
        # 画面部品変更
        widgets = {'text':forms.Textarea(attrs={'cols':80})}


