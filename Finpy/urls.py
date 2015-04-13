from django.conf.urls import include, patterns, url
from django.contrib.auth import views as auth_views
from Finpy import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^signup/$', views.signup, {'template_name': 'accounts/signup.html'}, name='signup'),
                        url(r'^entry/create/$', views.create_entry, name='create_entry'),
                        url(r'^entry/list/$', views.list_entry, name='list_entry'),
                        url(r'^entry/update/(?P<entry_id>\d+)$', views.update_entry, name='update_entry'),
                        url(r'^profile/update/(?P<profile_id>\d+)$', views.update_profile, name='update_profile'),
                        url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
                        url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
                        url(r'^password_change/$', auth_views.password_change, {'template_name': 'accounts/password_change_form.html'}, name='password_chage'),
                        url(r'^password_change/done/$', auth_views.password_change_done, {'template_name': 'accounts/password_change_done.html'}, name='password_change_done'),
                        url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'accounts/password_reset_form.html'}, name='password_reset'),
                        url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'accounts/password_reset_done.html'},name='password_reset_done'),
                        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                            auth_views.password_reset_confirm, {'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
                        url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
                       )
