from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'is_available', 'owner')
    list_filter = ('brand', 'is_available')
    search_fields = ('model', 'brand', 'owner__username')
