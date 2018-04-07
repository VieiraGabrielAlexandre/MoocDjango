from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
=======
	url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
    )
>>>>>>> 46ce90fe4035ea380c6e6b06ca8d29d0aacfcef6
