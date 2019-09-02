from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Book(models.Model):
    name =models.CharField(max_length=50,verbose_name="书名")
    price =models.FloatField(verbose_name="价格")
    body = RichTextUploadingField(config_name='my_config',default="hui")