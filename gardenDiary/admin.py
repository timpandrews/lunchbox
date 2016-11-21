from django.contrib import admin

from gardenDiary.models import post

class postAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "timestamp",
        "updated",
    ]
    list_display_links = ["title"]
    class Meta:
        model = post


admin.site.register(post, postAdmin)
