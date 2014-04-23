from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import send_zufang
import send_goods
import show_index
import send_car
from show_goods import goods_detail
from show_house import house_detail
from chat_room import chatroom
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wechat.views.home', name='home'),
    # url(r'^wechat/', include('wechat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^send_house/$',send_zufang.get_post),
    url(r'^send_qiuzu/$',send_zufang.get_qiuzu),
    url(r'^send_zhuanrang/$',send_goods.get_zhuanrang),
    url(r'^send_qiugou/$',send_goods.get_qiugou),
    url(r'^send_car/$',send_car.get_car),
    url(r'^$',show_index.show_index,name="show_index"),
    url(r'^house_detail/(\d+)/$',house_detail),
    url(r'^goods_detail/(\d+)/$',goods_detail),
    url(r'^chatroom/$',chatroom),
    url(r'^chat/', include('djangoChat.urls')),
    #url(r'^house_detail/(\d+)/$',house_detail),
)
urlpatterns += patterns('django.views.generic.simple',
    (r'^upload/$',TemplateView.as_view(template_name="upload_all.html")),
    (r'^upload_house/$',TemplateView.as_view(template_name="upload_house.html")),
    (r'^upload_goods/$',TemplateView.as_view(template_name="upload_goods.html")),
    (r'^upload_car/$',TemplateView.as_view(template_name="upload_car.html")),
    (r'^success/$',TemplateView.as_view(template_name="success.html")),
)

urlpatterns += patterns('',
(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)