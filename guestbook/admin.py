from django.contrib import admin

from guestbook.models import Message

@admin.register(Message)
class GuestMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_visible')