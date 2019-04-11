from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Workshop(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name=models.CharField(max_length=50,verbose_name="车间名称")
    status=models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS,verbose_name="状态")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name=verbose_name_plural='车间'
        ordering=['id']


class Computer(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name=models.CharField(max_length=50,verbose_name="名称")
    status=models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS,verbose_name="状态")
    os=models.CharField(max_length=30,verbose_name="操作系统")
    ip=models.CharField(max_length=15,verbose_name="IP")
    brand=models.CharField(max_length=30,verbose_name="品牌")
    serial_num=models.CharField(max_length=30,verbose_name="S/N码")
    discription=models.CharField(max_length=50,verbose_name="描述信息")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name=verbose_name_plural="电脑"


class Printer(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name=models.CharField(max_length=50,verbose_name="名称")
    status=models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS,verbose_name="状态")
    ip=models.CharField(max_length=15,verbose_name="IP")
    discription=models.CharField(max_length=50,verbose_name="描述信息")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name=verbose_name_plural="打印机"

class RepairInfor(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    title=models.CharField(max_length=50,verbose_name="标题")
    owner=models.ForeignKey(User,verbose_name="作者")
    discription=models.TextField(verbose_name="描述",help_text="请输入内容")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name=verbose_name_plural='维修记录'

class Station(models.Model):
    STATUS_NORMAL=1
    STATUS_DELETE=0
    STATUS_ITEMS=(
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )
    name=models.CharField(max_length=50,verbose_name="工位名称")
    status=models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS,verbose_name="状态")
    created_time=models.DateTimeField(auto_now_add=True,verbose_name="工位创建时间")
    pc=models.ForeignKey(Computer,verbose_name="主机")
    printer=models.ForeignKey(Printer,verbose_name="打印机")
    workshop=models.ForeignKey(Workshop,verbose_name="所属车间")
    repairinfor=models.ForeignKey(RepairInfor,verbose_name="维修信息")
    # ogb=models.ForeignKey(OGB,verbose_name="操作指导书")

    class Meta:
        verbose_name=verbose_name_plural='工位'

