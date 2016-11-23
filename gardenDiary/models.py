from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


def upload_location(instance, filename):
    return "%s/%s" %(instance.user_id, filename)

class post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    badge = models.ImageField(null=True, blank=True, upload_to=upload_location)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-id",] # default order for this table

    # returns the url (in the gardenDiary app) for new records
    def get_absolute_url(self):
        return reverse("gardenDiary:detail", kwargs={"id": self.id})