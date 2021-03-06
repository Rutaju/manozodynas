from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view
from .views import zodziai_view
from .views import NaujasZodis

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^zodziai/$', zodziai_view, name='zodziai'),
    url(r'^zodis/$', NaujasZodis.as_view(), name='zodis'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
