from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from bbs.models import Goods


def goods_detail(request,house_id):
    static_url = settings.STATIC_URL
    t = get_template('goods.html')
    goods = Goods.objects.get(id=house_id)
    html = t.render(Context({'STATIC_URL': static_url,"goods": goods}))
    return HttpResponse(html)