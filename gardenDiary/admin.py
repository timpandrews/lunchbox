from django.contrib import admin

from gardenDiary.models import post
from gardenDiary.models import profile

class postAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "timestamp",
        "updated",
    ]
    list_display_links = ["title"]
    ordering = ["-id"]
    class Meta:
        model = post


admin.site.register(post, postAdmin)
admin.site.register(profile)