from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'count.views.home', name='home'),
)
