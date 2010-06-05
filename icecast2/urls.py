from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('icecast2.views',
    url(r'^mount_points/$', 'mount_points', name='mount_points'),
)
