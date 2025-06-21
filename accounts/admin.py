from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'phone_number', 'is_seller')
    list_filter = ('is_seller',)
    search_fields = ('user__username', 'phone_number')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'اسم المستخدم'
