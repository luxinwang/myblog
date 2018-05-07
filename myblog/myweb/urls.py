"""myblog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'myweb'
urlpatterns = [

    # 博客首页
    url(r'^$', views.index, name = 'myweb_index'),
    url(r'^(?P<pIndex>[0-9]+)$', views.index, name = 'myweb_index'),
    # 文章详情页
    url(r'^post/(?P<pk>[0-9]+)$', views.detail, name = 'myweb_detail'),
    # 显示归档页面
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})$', views.archives,name = 'myweb_archives'),
    # 显示分类页面
    url(r'^category/(?P<pk>[0-9]+)$', views.category, name = 'myweb_category'),
    # 显示标签云页面
    url(r'^tag/(?P<pk>[0-9]+)$', views.tag, name = 'myweb_tag'),
    # 显示关于页面
    url(r'^about', views.about, name = 'myweb_about'),
    
    
]
