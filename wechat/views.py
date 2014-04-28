#coding=utf-8
from django.contrib import auth
from django.utils.timezone import now as utcnow
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from bbs.models import House, Goods, CarShare
from django.http import HttpResponseRedirect


def auto_login(req):
    if req.user.username and req.user.profile.is_chat_user:
        return True
    else:
        if req.method == 'GET':
            username = req.GET.get("u")
            password = req.GET.get("p")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(req, user)
                cu = req.user.profile
                cu.is_chat_user = True
                cu.last_accessed = utcnow()
                cu.save()
                return True
            else:
                return False
        return False

def index(request):
    if auto_login(request):
        static_url = settings.STATIC_URL
        t = get_template('index.html')
        house = House.objects.all().order_by("-timestamp")
        goods = Goods.objects.all().order_by("-timestamp")
        cars = CarShare.objects.all().order_by("-timestamp")
        count_cars = cars.count()
        count_house = house.count()
        count_goods = goods.count()
        html = t.render(Context({'STATIC_URL': static_url, "house": house,
        "count_house": count_house, "goods": goods, "count_goods": count_goods,
        "cars": cars, "count_cars": count_cars}))
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('/need_login')