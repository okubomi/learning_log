from django.urls import path, include
from . import views

#アプリフォルダ名{% url 'accounts:login' %}
app_name = 'accounts'

# urlアドレスと関数の紐づけ
urlpatterns = [
    # ドメイン名のルート /accounts/login/  /accounts/logout/
    path('', include('django.contrib.auth.urls')),
    # ユーザー登録 /accounts/register/
    path('register', views.register,name='register'),
]
