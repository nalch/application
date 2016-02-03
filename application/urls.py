from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url
)
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^application/', include('nalch_application.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
