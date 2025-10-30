from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)