#coding=utf-8
from django.db import models

class House(models.Model):
    oid = models.CharField(max_length=50)
    name = models.CharField('用户名',max_length=20)
    room = models.CharField('类型',max_length=20)
    timestamp = models.DateTimeField('时间',auto_now=True)
    category = models.CharField('分类',max_length=10)
    phone = models.CharField('电话',max_length=20)
    dist = models.CharField('区域',max_length=20)
    addr = models.CharField('地址',max_length=100)
    pic = models.CharField('图片',max_length=50)
    price = models.CharField('价格',max_length=20)
    note = models.TextField('备注')

    class Meta:
        verbose_name = "租房信息"
        verbose_name_plural = "租房信息"  
