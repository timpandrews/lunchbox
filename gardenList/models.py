from __future__ import unicode_literals

from django.conf import settings
from django.db import models

class following(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    followingID = models.IntegerField()

    def __unicode__(self):
        return self.title
