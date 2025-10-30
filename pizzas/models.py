from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.name
    
class Topping(models.Model):
    """トピックに関して学んだ具体的なこと"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        """モデルの文字列表現を返す"""
        return self.name
