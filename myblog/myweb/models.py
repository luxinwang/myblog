from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# 文章分类
class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

# 文章标签
class Tag(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

# 文章主体
class Post(models.Model):
    def __str__(self):
        return self.title
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 文章创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 文章最后一次修改时间
    modified_time = models.DateTimeField(auto_now_add=True)
    # 文章摘要，允许为空
    excerpt = models.CharField(max_length=200,blank=True)
    # 文章分类
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # 文章标签,可以为空
    tags = models.ManyToManyField(Tag,blank=True)
    # 文章作者
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # 文章阅读量
    views = models.PositiveIntegerField(default=0)
    
    # 重定向到文章所对应的url
    def get_absolute_url(self):
        return reverse('myweb:myweb_detail',kwargs={'pk':self.pk})

    # 统计文章阅读数
    def increase_views(self):
        self.views += 1
        self.save(update_fields = ['views'])

    # 复写save方法，自动生成摘要
    def save(self,*args,**kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化MarkDown类，渲染body文本
            md = markdown.Markdown(extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite'
                ])
            # 去掉html标签并摘取前54个字符赋给excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        # 调用父类save方法将数据保存到数据库
        super(Post,self).save(*args,**kwargs)


    # 默认按文章发布时间倒序显示
    class Meta:
        ordering = ['-create_time','title']
