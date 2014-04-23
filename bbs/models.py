#coding=utf-8
from django.db import models

class House(models.Model):
    #oid = models.CharField(max_length=50)
    name = models.CharField('用户名',max_length=20)
    room = models.CharField('类型',max_length=20)
    timestamp = models.DateTimeField('时间',auto_now=True)
    category = models.CharField('分类',max_length=10)
    phone = models.CharField('电话',max_length=20)
    dist = models.CharField('区域',max_length=20)
    addr = models.CharField('地址',max_length=100)
    pic = models.ImageField('图片',upload_to="house_pic",null=True,blank=True)
    pic2 = models.ImageField('图片',upload_to="house_pic",null=True,blank=True)
    pic3 = models.ImageField('图片',upload_to="house_pic",null=True,blank=True)
    price = models.CharField('价格',max_length=20)
    note = models.TextField('备注',null=True,blank=True)

    class Meta:
        verbose_name = "租房信息"
        verbose_name_plural = "租房信息"

    def image_tag(self):
        img_path = ""
        if (str(self.pic)!=""):
            img_path = '<img src="/media/'+ str(self.pic) + '"/><p/>'

        if (str(self.pic2)!=""):
            img_path += '<img src="/media/'+ str(self.pic2) + '"/><p/>'

        if (str(self.pic3)!=""):
            img_path += '<img src="/media/'+ str(self.pic3) + '"/>'
        return img_path

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Chat_room(models.Model):
    name = models.CharField('用户名',max_length=20)
    messages = models.CharField('内容',max_length=300)
    timestamp = models.DateTimeField('时间',auto_now=True)


class Goods(models.Model):
    name = models.CharField('用户名',max_length=20)
    timestamp = models.DateTimeField('时间',auto_now=True)
    goods_name = models.CharField('名称',max_length=50)
    category = models.CharField('分类',max_length=10)
    phone = models.CharField('电话',max_length=20)
    dist = models.CharField('区域',max_length=20)
    pic = models.ImageField('图片',upload_to="house_pic",null=True,blank=True)
    pic2 = models.ImageField('图片',upload_to="house_pic",null=True,blank=True)
    pic3 = models.ImageField('图片',upload_to="house_pic",null=True,blank=True)
    price = models.CharField('价格',max_length=20)
    note = models.TextField('备注',null=True,blank=True)

    class Meta:
        verbose_name = "二手物品"
        verbose_name_plural = "二手物品"

    def image_tag(self):
        img_path = ""
        if (str(self.pic)!=""):
            img_path = '<img src="/media/'+ str(self.pic) + '"/><p/>'

        if (str(self.pic2)!=""):
            img_path += '<img src="/media/'+ str(self.pic2) + '"/><p/>'

        if (str(self.pic3)!=""):
            img_path += '<img src="/media/'+ str(self.pic3) + '"/>'
        return img_path

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class CarShare(models.Model):
    name = models.CharField('用户名',max_length=20)
    timestamp = models.DateTimeField('时间',auto_now=True)
    phone = models.CharField('电话',max_length=20)
    from_addr = models.CharField('起点',max_length=100)
    to_addr = models.CharField('终点',max_length=100)
    note = models.TextField('备注',null=True,blank=True)
