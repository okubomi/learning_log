from django.urls import path
from . import views

#アプリフォルダ名{% url 'leaning_logs:index' %}
app_name = 'pizzas'

# urlアドレスと関数の紐づけ
urlpatterns = [
    # ドメイン名/pizzas/
    path('', views.index, name='index'),
    # ピザ一覧
    path('pizzas/', views.pizzas, name='pizzas'),
    # 1つのピザに紐づいたトッピング一覧
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]