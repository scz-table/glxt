from django.db import models
from django.utils.timezone import datetime,now,make_aware
from django.contrib.auth.models import User
import pytz

class BasicData(models.Model):
    groupName=models.CharField(max_length=100,verbose_name="组名称")
    groupNameRemarks=models.CharField(max_length=256,null=True,blank=True,verbose_name="组备注")
    projectName=models.CharField(max_length=100,verbose_name="项目名称")
    projectNameRemarks=models.CharField(max_length=256,null=True,blank=True,verbose_name="项目备注")
    projectDict=models.CharField(max_length=100,verbose_name="项目字典")
    projectKey=models.CharField(max_length=100,verbose_name="项目字典关键字")
    projectValue=models.CharField(max_length=100,verbose_name="项目字典值")
    projectValueRemarks=models.CharField(max_length=256,null=True,blank=True,verbose_name="项目字典值备注")
    projectExtend1=models.CharField(max_length=100,null=True,blank=True,verbose_name="项目备用1")
    projectExtend2=models.CharField(max_length=100,null=True,blank=True,verbose_name="项目备用2")
    projectExtend3=models.CharField(max_length=100,null=True,blank=True,verbose_name="项目备用3")
    projectExtend4=models.CharField(max_length=100,null=True,blank=True,verbose_name="项目备用4")
    projectExtend5=models.CharField(max_length=100,null=True,blank=True,verbose_name="项目备用5")
    # createTime=models.DateTimeField(auto_now_add=True)
    # changeTime=models.DateTimeField(auto_now=True,default=make_default_time())
    lastEditName=models.ForeignKey(User,on_delete=models.CASCADE,related_name='basicDataLastEditName',verbose_name="最后编辑员工")
    createName=models.ForeignKey(User,on_delete=models.CASCADE,related_name='basicDataCreateName',verbose_name="创建记录员工")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        db_table='basicData'
        verbose_name_plural = '基础数据'
        ordering=("groupName","projectName","projectDict","projectKey","projectValue")

    def __str__(self):
        return self.groupName