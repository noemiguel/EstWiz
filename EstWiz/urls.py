from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'EstWiz.views.home', name='home'),
    url(r'^bid/', include('bid.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
