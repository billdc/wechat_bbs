from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from bbs.models import House

def house_detail(request,house_id):
    static_url = settings.STATIC_URL
    t = get_template('house.html')
    house = House.objects.get(id=house_id)
    html = t.render(Context({'STATIC_URL': static_url,"house":house}))
    return HttpResponse(html)