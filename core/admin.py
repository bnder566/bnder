from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name_display', 'email_display', 'created_at_display')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

    def name_display(self, obj):
        return obj.name
    name_display.short_description = 'الاسم'

    def email_display(self, obj):
        return obj.email
    email_display.short_description = 'البريد الإلكتروني'

    def created_at_display(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M')
    created_at_display.short_description = 'تاريخ الإرسال'
