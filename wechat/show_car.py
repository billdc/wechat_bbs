from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from bbs.models import CarShare


def car_detail(request,car_id):
    static_url = settings.STATIC_URL
    t = get_template('carshare.html')
    car = CarShare.objects.get(id=car_id)
    html = t.render(Context({'STATIC_URL': static_url,"car": car}))
    return HttpResponse(html)