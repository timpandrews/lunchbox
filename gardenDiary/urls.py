from django.conf.urls import url
from gardenDiary.views import (home, )

urlpatterns = [
    url(r'^$', home, name="home"),
]
