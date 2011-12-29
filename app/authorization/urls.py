# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
#
urlpatterns = patterns('authorization.views',
    url(r'^$','profile_show',name = 'authorization.profile_show'),
    url(r'^register$','register',name = 'authorization.register'),
)
    #url(r'^(?P<news_id>\d+)/$','news_detail',name = 'news.news_detail'),) # тема стала ссылкой и так работает тут через заглушку
