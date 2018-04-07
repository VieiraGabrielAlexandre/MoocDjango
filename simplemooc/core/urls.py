from django.conf.urls import patterns, include, url

<<<<<<< HEAD
urlpatterns = patterns('simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)
=======
urlpatterns = patterns('',
   	url(r'^$', 'simplemooc.core.views.home', name='home'),
   	url(r'inicio/$', 'simplemooc.core.views.home', name='home'),
   	url(r'contato/$', 'simplemooc.core.views.contact', name='contact'),
    	)
>>>>>>> 46ce90fe4035ea380c6e6b06ca8d29d0aacfcef6
