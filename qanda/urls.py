from django.conf.urls.defaults import *

urlpatterns = patterns('qanda.views',
    (r'^$', 'index'),
    (r'^answers/$', 'answers'),
)
