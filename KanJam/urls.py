from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'KanJam.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^finpy/', include('Finpy.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
