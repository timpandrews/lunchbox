from django.conf.urls import url
from gardenDiary.views import (
    gardenDiary,
    gardenDiary_create,
    gardenDiary_update,
    gardenDiary_detail,
    gardenDiary_delete,
)

urlpatterns = [
    url(r'^$', gardenDiary, name="list"),
    url(r'^create/$', gardenDiary_create, name="create"),
    url(r'^(?P<id>\d+)/edit/$', gardenDiary_update, name="update"),
    url(r'^(?P<id>\d+)/$', gardenDiary_detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/', gardenDiary_delete, name="delete"),
]
