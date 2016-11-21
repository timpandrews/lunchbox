from django.conf.urls import url
from gardenDiary.views import (home, gardenDiary)

urlpatterns = [
    url(r'^$', gardenDiary, name="gardenDiary"),
]
