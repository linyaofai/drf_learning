from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app01.serializers import *
from app01.models import Book
import logging
collect_logger = logging.getLogger("collect")
logger = logging.getLogger(__name__)
# Create your views here.
class UserInfoView(ModelViewSet):
    logger.debug("一个萌萌的请求过来了。。。。")
    logger.info("一个更萌的请求过来了。。。。")
    logger.debug("这是app01里面的index视图函数")

    collect_logger.info("用户1:河南")
    queryset = Book.objects.all()
    serializer_class = UserInfoSerializer