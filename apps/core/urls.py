#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.core.views',
    url(r'home/$', 'home', name='home'),
    url(r'^solicitacoes/$', 'solicitations', name='solicitations'),
    url(r'^solicitacoes/add/$', 'solicitation_add', name='solicitation-add'),
    url(r'^configuracoes/', 'settings', name='settings'),
)

# Login views
urlpatterns += patterns(
    '',

    # login view
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),

    # logout view
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/home'}, name='logout'),
)
