from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$', open_orders, name='index'),
    url(r'^create$', create_order, name='opening'),
    #url(r'^articles/person/(?P<person_id>\d+)$', noticias_por_persona, name='news_by_person'),
)