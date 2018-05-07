from django.shortcuts import render,get_object_or_404,redirect
from myweb.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.


def post_comment(request,post_pk):
    # 获取被评论的文章
    post = get_object_or_404(Post,pk=post_pk)
    # 判断用户请求是否为POST请求,是则处理表单数据
    if request.method == 'POST':
        # 生成表单
        form = CommentForm(request.POST)

        # 调用 form.is_valid方法，检查表单数据是否符合要求

        if form.is_valid():

            # commit=False 作用是仅利用表单数据生成Comment实例，还不保存进数据库

            comment = form.save(commit=False)
            # 将评论与文章关联
            comment.post = post
            comment.save()
            # 重定向到文章详情页
            return redirect(post)

        else:
            # 数据不合法则重新渲染详情页
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list' : comment_list
                       }

            return render(request,'blog/detail.html',context)

    # 不是POST请求，说明用户未提交数据，重定向到文章详情页
    return redirect(post)

    
