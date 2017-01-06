from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save


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



class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return str(self.user.username)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)