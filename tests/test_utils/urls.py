import django
import django.contrib.sitemaps.views
import django.views.i18n
import django.views.static
from django.conf import settings
from django.contrib import admin

if django.VERSION[:2] >= (2, 0):
    from django.urls import include, re_path as url
else:
    from django.conf.urls import include, url

urlpatterns = [
    url(r'^media/(?P<path>.*)$', django.views.static.serve,  # NOQA
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^', include('ads_txt.urls')),  # NOQA
]
