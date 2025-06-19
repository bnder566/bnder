from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات المخصصة
    path('accounts/', include('accounts.urls')),     # تسجيل الدخول والتسجيل
    path('inventory/', include('inventory.urls')),   # بيانات السيارات
    path('', include('core.urls')),                  # الصفحة الرئيسية وصفحات عامة
]
