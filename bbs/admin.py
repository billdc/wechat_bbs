#coding=utf-8
from django.contrib import admin
from bbs.models import House,Goods

class HouseAdmin(admin.ModelAdmin):
    list_display = ('category','dist','note','timestamp')
    readonly_fields = ('image_tag',)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('category','goods_name','dist','note','timestamp')
    readonly_fields = ('image_tag',)

admin.site.register(House,HouseAdmin)
admin.site.register(Goods,GoodsAdmin)