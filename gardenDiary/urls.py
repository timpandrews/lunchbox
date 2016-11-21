from django.conf.urls import url
from gardenDiary.views import (
    gardenDiary,
    gardenDiary_create,
    gardenDiary_update,
    gardenDiary_detail,
    gardenDiary_delete,
)

urlpatterns = [
    url(r'^$', gardenDiary, name="gardenDiary"),
    url(r'^create/$', gardenDiary_create, name="create"),
    url(r'^update/$', gardenDiary_update, name="update"),
    url(r'^(?P<id>\d+)$', gardenDiary_detail, name="detail"),
    url(r'^delete/', gardenDiary_delete, name="delete"),
]
