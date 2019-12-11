from django.db import models
from django.contrib.auth.models import User
from Department.models import Position

# 代理模式建立表关系
# Person.objects.all()
# User.objects.all()
# 以上两种写法是一样的

# class Person(User):
#     class Meta:
#         proxy=True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)
#
#
#     def get_username(cls):
#         return cls.email
#
#     @property
#     def get_testproperty(self):
#         return self.username

# 一对一的建立表关系
class UserExtension(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension',verbose_name="用户名")
    fullname=models.CharField(max_length=100,verbose_name="姓名")
    telephone=models.CharField(max_length=11,unique=True,verbose_name="手机")
    phone=models.CharField(max_length=13,verbose_name="座机")
    school=models.CharField(max_length=200,null=False,blank=True,verbose_name="学校")
    profession=models.CharField(max_length=200,null=False,blank=True,verbose_name="专业")
    address=models.CharField(max_length=200,null=False,blank=True,verbose_name="居住住址")
    aboutme=models.CharField(max_length=200,null=False,blank=True,verbose_name="自我介绍")
    photo=models.ImageField(null=False,blank=True,verbose_name="照片")
    position=models.ManyToManyField(Position,related_name='UserPosition',verbose_name="职位")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        db_table='auth_user_userextension'
        verbose_name_plural = '扩展用户信息'
        ordering=("-create_time",)
        permissions = (
            ("sepecial", "Can publish article"),
        )
    def __str__(self):
        return self.fullname


# @receiver(post_save,sender=User)
# def handler_user_extension(sender,instance,created,**kwargs):
#     if created:
#         print('新建userExtension')
#         UserExtension.objects.create(user=instance)
#     else:
#         print('保存userExtension')
#         instance.extension.save()