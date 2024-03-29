"""drf_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app01.views import UserInfoView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
router =DefaultRouter()
router.register('users',UserInfoView,base_name='user')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'docs/', include_docs_urls(title='接口文档')),  # 接口路径
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns +=router.urls
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)