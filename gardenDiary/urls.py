from django.conf.urls import url
from gardenDiary.views import (gardenDiary_home, )

urlpatterns = [
    url(r'^$', gardenDiary_home, name="home"),
]
