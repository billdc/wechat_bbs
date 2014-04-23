#coding=utf-8
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from bbs.models import House
import Image as image
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def get_value(req,request):
    if request.POST.get(req) != '':
        return request.POST.get(req)
    else:
        return ""

def resizeImg(img):
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

def get_post(request):
    post_data="no post"
    if request.method == 'POST':
        name = get_value("name",request)
        phone = get_value("phone",request)
        addr = get_value("addr",request)
        dist = get_value("dist",request)
        price = get_value("price",request)
        note = get_value("note",request)
        room = get_value("room",request)
        category = get_value("category",request)
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

        house = House(
                name = name,
                room = room,
                category = category,
                phone = phone,
                dist = dist,
                addr = addr,
                pic = new_img1,
                pic2 = new_img2,
                pic3 = new_img3,
                price = price,
                note = note,
        )
        house.save()
    return HttpResponseRedirect('/success')

def get_qiuzu(request):
    post_data=request.POST
    if request.method == 'POST':
        name = get_value("qname",request)
        phone = get_value("qphone",request)
        addr = get_value("qaddr",request)
        dist = get_value("qdist",request)
        price = get_value("qprice",request)
        note = get_value("qnote",request)
        room = get_value("qroom",request)
        category = get_value("category",request)
        house = House(
                name = name,
                room = room,
                category = category,
                phone = phone,
                dist = dist,
                addr = addr,
                price = price,
                note = note,
        )
        house.save()

    return HttpResponse(post_data)