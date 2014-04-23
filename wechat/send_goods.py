#coding=utf-8
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from bbs.models import Goods
import Image as image
import re
from django.core.context_processors import csrf

def get_value(req,request):
    if request.POST.get(req) != '':
        return request.POST.get(req)
    else:
        return ""

def resizeImg(img):
    if re.search(r'.+(\.jpg$)|(\.JPEG$)|(\.JPG$)|(\.jpeg$)|(\.png$)|(\.gif$)|(\.bmp$)',img.name):
        new_img = image.open(img)
        img_width,img_height = new_img.size
        if (img_width > 200 ):
            tempfile_io =StringIO.StringIO()
            ratio = 200.0/float(img_width)
            new_img_width = int(img_width * ratio)
            new_img_height = int(img_height * ratio)
            new_img.resize((new_img_width,new_img_height),image.ANTIALIAS).save(tempfile_io,format="png",quality=90)
            image_file = InMemoryUploadedFile(tempfile_io, None, "upload.jpg",'image/jpeg',tempfile_io.len, None)
            return image_file
        return img
    else:
        return ""

def get_zhuanrang(request):
    post_data="no post"
    if request.method == 'POST':
        name = get_value("name",request)
        phone = get_value("phone",request)
        dist = get_value("dist",request)
        price = get_value("price",request)
        note = get_value("note",request)
        category = get_value("category",request)
        goods_name = get_value("goods_name",request)
        if 'img1' in request.FILES:
            img1 = request.FILES["img1"]
            new_img1 = resizeImg(img1)
        else:
            new_img1=None

        if 'img2' in request.FILES:
            img2 = request.FILES["img2"]
            new_img2 = resizeImg(img2)
        else:
            new_img2=None

        if 'img3' in request.FILES:
            img3 = request.FILES["img3"]
            new_img3 = resizeImg(img3)
        else:
            new_img3=None

        goods = Goods(
                name = name,
                category = category,
                goods_name = goods_name,
                phone = phone,
                dist = dist,
                pic = new_img1,
                pic2 = new_img2,
                pic3 = new_img3,
                price = price,
                note = note,
        )
        goods.save()

    post_data="""
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
    提交成功！请等待审核后发布！
    </div>
    </body>
    </html>
    """
    return HttpResponse(post_data)

def get_qiugou(request):
    post_data=request.POST
    if request.method == 'POST':
        name = get_value("qname",request)
        phone = get_value("qphone",request)
        goods_name = get_value("qgoods_name",request)
        dist = get_value("qdist",request)
        price = get_value("qprice",request)
        note = get_value("qnote",request)
        category = get_value("category",request)
        goods = Goods(
                name = name,
                category = category,
                goods_name = goods_name,
                phone = phone,
                dist = dist,
                price = price,
                note = note,
        )
        goods.save()

    return HttpResponse("chenggong")