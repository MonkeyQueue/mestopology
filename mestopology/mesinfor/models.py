from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class MainInfor(models.Model):
#     STATUS_NORMAL=1
#     STATUS_DELETE=0
#     STATUS_ITEMS=(
#         (STATUS_NORMAL,'正常'),
#         (STATUS_DELETE,'删除'),
#     )
#     name=models.CharField(max_length=50,verbose_name="名称")
#     status=models.PositiveIntegerField(default=STATUS_NORMAL,
#         choices=STATUS_ITEMS,verbose_name="状态")
#     station=models.ForeignKey(Station,verbose_name="所属车间")
#     pc=models.ForeignKey(PC,verbose_name="主机")
#     printer=models.ForeignKey(Printer,verbose_name="打印机")
#     created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

#     class Meta:
#         verbose_name=verbose_name_plural='主信息'


class OGB(models.Model):
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
        verbose_name_plural=verbose_name_plural='操作指导书'
