from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from bbs.models import House

def show_index(request):
    static_url=settings.STATIC_URL
    t = get_template('index.html')
    house = House.objects.all()

    html = t.render(Context({'STATIC_URL': static_url,"house":house}))
    return HttpResponse(html)