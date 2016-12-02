from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from gardenDiary.views import home, gardeners, tools

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^gardenDiary/', include("gardenDiary.urls", namespace="gardenDiary")),
    url(r'^gardeners/', gardeners, name="garderners"), # add namespace when I create new app
    url(r'^tools/', tools, name="tools"), # add namespace when I create new app
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)