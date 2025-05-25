from django.contrib import admin

from guestbook.models import Message

@admin.register(Message)
class GuestMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_visible',)
    search_fields = ('name', 'email', 'text',)
    list_filter = ('is_visible', 'created_at',)
    readonly_fields = ('created_at',)
    # fields = ('name', 'text', 'is_visible', 'admin_reply',)