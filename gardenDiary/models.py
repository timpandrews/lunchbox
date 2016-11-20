from __future__ import unicode_literals

from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title
