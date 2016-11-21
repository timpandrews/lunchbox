from django.conf.urls import url
from gardenDiary.views import (gardenDiary, gardeners)

urlpatterns = [
    url(r'^$', gardenDiary, name="gardenDiary"),
]
