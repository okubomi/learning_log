from django.urls import path
from . import views

#アプリフォルダ名{% url 'leaning_logs:index' %}
app_name = 'learning_logs'

# urlアドレスと関数の紐づけ
urlpatterns = [
    # ドメイン名のルート
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # topics/1/  １つのトピックについての処理なので単数形
    # def topic(topic_id)
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # topic 新規登録
    path('new_topic/', views.new_topic, name='new_topic'),
    # entry 新規登録 /new_entry/1/
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
        # entry 編集 /edit_entry/1/
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
