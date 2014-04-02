#coding=utf-8
from django.contrib import admin
from bbs.models import House

class HouseAdmin(admin.ModelAdmin):
    list_display = ('category','dist','note','timestamp')

admin.site.register(House,HouseAdmin)
