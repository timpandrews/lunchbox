from django.contrib import admin

from gardenList.models import following

class followingAdmin(admin.ModelAdmin):
    class Meta:
        model = following

    list_display = [
        "account",
        "following",
    ]

    ordering = ["account", "following"]


admin.site.register(following, followingAdmin)
