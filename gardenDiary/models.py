from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    badge = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-id",] # default order for this table

    # returns the url (in the gardenDiary app) for new records
    def get_absolute_url(self):
        return reverse("gardenDiary:detail", kwargs={"id": self.id})