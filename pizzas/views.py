from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'pizzas/index.html')
    # return HttpResponse('pizzas:index.html OK!')  
from .models import Pizza
def pizzas(request):
    # ピザレコードを全件検索
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request,'pizzas/pizzas.html',context)

# 'pizzas/<int:pizza_id>/'
def pizza(request, pizza_id):
    # idでピザを検索
    pizza = Pizza.objects.get(id=pizza_id)
    # 検索したピザに紐づいたトッピング一覧を取得
    toppings = pizza.topping_set.all()
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request,'pizzas/pizza.html',context)