from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    departmentName=models.CharField(max_length=200,unique=True,verbose_name="部门名称")
    remarksInformation=models.CharField(max_length=255,null=False,blank=True,verbose_name="备注信息")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        db_table='department'
        verbose_name_plural = '部门'
        ordering=("-create_time",)
    def __str__(self):
        return self.departmentName

class Position(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department_position',verbose_name="部门")
    position = models.CharField(max_length=100, verbose_name="职位")
    remarksInformation=models.CharField(max_length=255,null=False,blank=True,verbose_name="备注信息")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    change_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    class Meta:
        db_table='department_position'
        verbose_name_plural = '职位'
        ordering=("-create_time",)
    def __str__(self):
        return "%s %s"%(self.department.departmentName,self.position)