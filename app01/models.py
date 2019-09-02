from django.db import models

# Create your models here.

class Book(models.Model):
    name =models.CharField(max_length=50,verbose_name="书名")
    price =models.FloatField(verbose_name="价格")
