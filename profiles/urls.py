from django.conf.urls import url
from profiles.views import (
    UserDetailView,
)

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name="detail"),
]
