from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app01.serializers import *
from app01.models import Book
# Create your views here.
class UserInfoView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = UserInfoSerializer