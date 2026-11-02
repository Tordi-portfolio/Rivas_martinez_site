from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "created", "is_read")
    list_filter = ("service", "is_read")
    search_fields = ("name", "email", "message")
