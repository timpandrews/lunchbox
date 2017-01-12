from __future__ import unicode_literals

from django.conf import settings
from django.db import models

class following(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='account', default=1)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', default=1)


    def __unicode__(self): # python 2
        return str(self.account)

    def __str__(self): # python 3
        return str(self.account)



