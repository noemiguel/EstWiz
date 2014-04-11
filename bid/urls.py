from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^get/(?P<bid_id>\d+)/$', 'bid.views.bid'),
    url(r'^form/', 'bid.views.bid_form'),
    url(r'^form_submit/', 'bid.views.bid_form_submit'),
    url(r'^list/','bid.views.bid_list'),
)
