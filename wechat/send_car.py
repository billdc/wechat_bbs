#coding=utf-8
from django.http import HttpResponse
from bbs.models import CarShare
from django.core.context_processors import csrf

def get_value(req,request):
    if request.POST.get(req) != '':
        return request.POST.get(req)
    else:
        return ""


def get_car(request):
    if request.method == 'POST':
        name = get_value("name",request)
        phone = get_value("phone",request)
        from_addr = get_value("from_addr",request)
        to_addr = get_value("to_addr",request)
        note = get_value("note",request)
        start_time = get_value("start_time",request)
        car = CarShare(
                name = name,
                from_addr = from_addr,
                to_addr = to_addr,
                phone = phone,
                note = note,
                start_time = start_time,
        )
        car.save()

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