#coding=utf-8
from django.db import models,connection
from django.contrib.auth.models import User

class Blog_essayManager(models.Manager):
    def study_title_id(self):
        cursor=connection.cursor()
        cursor.execute('''
        select title,tag_id 
        from mydb_blog_essay 
        where tag_id not in (select id from mydb_blog_tag where tag_name="工具" or tag_name="生活") 
        order by createtime desc ;''')
        row=cursor.fetchall()
        return row


# Create your models here.
class Blog_user(models.Model):
    user = models.OneToOneField(User)
    portrait = models.ImageField(upload_to='portrait_img/',default='portrait_img/user.jpg')
    signature = models.CharField('签名',max_length=20,default='Say . what..',blank=True)
    gender = models.CharField('性别',max_length=1,choices=(('m','man'),('w','woman')),blank=True)

    def __unicode__(self):
        return self.user.username

class Blog_tag(models.Model):
    tag_name = models.CharField('标签',max_length=20,unique=True)

    def __unicode__(self):
        return self.tag_name

class Blog_essay(models.Model):
    title = models.CharField('文章名',max_length=30)
    content = models.TextField('文章内容')
    createtime = models.DateTimeField('创建时间',auto_now_add=True,null=True,blank=True)
    lastchange = models.DateTimeField('修改时间',null=True,blank=True)
    praise = models.IntegerField('点赞',default=0)
    page_view = models.IntegerField('浏览量',default=0)
    tag = models.ForeignKey(Blog_tag)
    top = models.IntegerField('置顶',default=0)

    objects=models.Manager()
    study_objects=Blog_essayManager()

    def __unicode__(self):
        return self.title
    class Meta:
        ordering=["-createtime"]

class Blog_comment(models.Model):
    blog_user = models.ForeignKey(Blog_user)
    blog_essay = models.ForeignKey(Blog_essay)
    comment = models.CharField('评论',max_length=255)
    comtime = models.DateTimeField('留言时间',auto_now_add=True)
    comtype = models.IntegerField('主楼or楼中楼',default=0)
    compraise = models.IntegerField('评论点赞',default=0)

    def __unicode__(self):
        return self.comment

class Blog_log(models.Model):
    blog_user = models.ForeignKey(Blog_user)
    action = models.CharField('用户动作',max_length=8,choices=(('login','登录'),
                                                               ('register','注册'),
                                                               ('logout','登出')
                                                               ))
    logtime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.action


#首页励志
class Blog_inspire(models.Model):
    inspire = models.TextField('励志微语')
