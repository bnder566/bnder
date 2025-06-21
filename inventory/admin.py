from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand_display', 'model_display', 'year_display', 'price_display', 'availability_display', 'owner_display')
    list_filter = ('brand', 'is_available')
    search_fields = ('model', 'brand', 'owner__username')

    def brand_display(self, obj):
        return obj.brand
    brand_display.short_description = 'العلامة التجارية'

    def model_display(self, obj):
        return obj.model
    model_display.short_description = 'الطراز'

    def year_display(self, obj):
        return obj.year
    year_display.short_description = 'سنة الصنع'

    def price_display(self, obj):
        return f"{obj.price:,.2f}"
    price_display.short_description = 'السعر'

    def availability_display(self, obj):
        return 'نعم' if obj.is_available else 'لا'
    availability_display.short_description = 'متوفر'

    def owner_display(self, obj):
        return obj.owner.username
    owner_display.short_description = 'المالك'
