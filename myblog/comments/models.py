from django.db import models

# Create your models here.

class Comment(models.Model):
    # 评论人姓名
    name = models.CharField(max_length=100)
    # 评论人邮箱
    email = models.EmailField(max_length=255)
    # 评论内容
    content = models.TextField()
    # 评论时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 所评论的文章
    post = models.ForeignKey('myweb.Post',on_delete=models.CASCADE)


    def __str__(self):
        return self.content[:20]
