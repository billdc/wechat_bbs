from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from bbs.models import House, Goods, CarShare


def show_index(request):
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