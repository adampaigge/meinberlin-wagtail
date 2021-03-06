from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from meinberlin import views as meinberlin_views

from search import views as search_views


urlpatterns = [
    url(r'^w/django-admin/', include(admin.site.urls)),

    url(r'^w/admin/', include(wagtailadmin_urls)),
    url(r'^w/documents/', include(wagtaildocs_urls)),

    url(r'^w/search/$', search_views.search, name='search'),

    url(r'^w/feedback/$', meinberlin_views.feedback_view, name='feedback'),

    url(r'w/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
