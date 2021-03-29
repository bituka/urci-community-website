from django.contrib import admin

from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('announcement_text', 'pub_date')

admin.site.register(Announcement, AnnouncementAdmin)