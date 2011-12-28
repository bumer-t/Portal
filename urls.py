# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout #авотризация
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration.forms import RegistrationFormUniqueEmail 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^news/', include('news.urls')),   #при переходе к news/ будут подгружаться URL-карты, относящиеся к приложению.
     (r'^profile/', include('authorization.urls')),
     url(r'^register/$', 'registration.views.register',{'form': RegistrationFormUniqueEmail}, name='registration_register'),
     (r'^accounts/', include('registration.urls')),
     url(r'^$', 'portal.authorization.views.auth_show'),
     
)

#при обращении к корню сервера - шаблон index.html. 
#urlpatterns += patterns('django.views.generic.simple',
#    (r'^$','direct_to_template', {'template': 'index.html'}),)

#для авторизации
#urlpatterns += patterns('',
#    #(r'^accounts/login/$', login),
#    #(r'^accounts/logout/$', logout),
#)
urlpatterns += staticfiles_urlpatterns()
