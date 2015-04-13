from django.conf.urls import patterns, include, url
from django.contrib import admin
from Finpy import views

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', views.index, name='finpy'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^finpy/', include('Finpy.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
