from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^register/', 'loginsys.views.register'),
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
)
