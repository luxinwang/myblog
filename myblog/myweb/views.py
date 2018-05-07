from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import *
import os,time
import markdown

from comments.forms import CommentForm
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.db.models import Q 
from django.core.paginator import Paginator 

# Create your views here.


# 前端博客首页
def index(request,pIndex=1):
    # 接收搜索条件
    q = request.GET.get('sou')
    if q:
        post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
        pIndex = int(pIndex)
        # 实例化分页类
        paginator = Paginator(post_list,6)
        # 获取分页数据对象
        list2 = paginator.page(pIndex)

        # 保存搜索条件
        wherestr = 'sou=' + q 
        # 分配数据
        context = {'post_list' : list2,'where' : wherestr}

        # 加载首页模板
        return render(request,'blog/index.html',context)
    else:
        # 获取文章
        post_list = Post.objects.all()
        pIndex = int(pIndex)
        # 实例化分页类
        paginator = Paginator(post_list,6)
        # 获取分页数据对象
        list2 = paginator.page(pIndex)
        # 分配数据
        context = {'post_list' : list2}

        # 加载首页模板
        return render(request,'blog/index.html',context)

# 文章详情页
def detail(request,pk):
    # 获取文章详情
    post = get_object_or_404(Post, pk=pk)
    # 阅读量+1
    post.increase_views()
    # 代码高亮
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    form = CommentForm()
    # 获取文章全部评论
    comment_list = post.comment_set.all()
    # 分配数据
    context = {'post' : post,'form':form,'comment_list':comment_list}
    # 加载模板
    return render(request,'blog/detail.html',context)

# 显示归档页
def archives(request,year,month):
    # 获取文章
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
        )
    # 分配数据
    context = {'post_list':post_list}
    # 加载模板
    return render(request,'blog/index.html',context)

# 显示分类页
def category(request,pk):
    # 获取分类名
    cate = get_object_or_404(Category,pk=pk)
    # 获取文章并分配数据
    post_list = Post.objects.filter(category=cate)
    context = {'post_list':post_list}
    # 加载模板
    return render(request,'blog/index.html',context)

# 显示标签云页面
def tag(request,pk):
    # 获取标签名
    tag_name = get_object_or_404(Tag,pk=pk)
    # 获取文章并分配数据
    post_list = Post.objects.filter(tags=tag_name)
    context = {'post_list':post_list}
    # 加载模板
    return render(request,'blog/index.html',context)

# 显示关于页面
def about(request):
    # 返回模版
    return render(request,'blog/about.html')
