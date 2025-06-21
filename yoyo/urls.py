from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('accounts/', include('accounts.urls', namespace='accounts')),   # تسجيل الدخول والتسجيل
    path('inventory/', include('inventory.urls', namespace='inventory')), # السيارات
    path('', include('core.urls', namespace='core')),                     # الصفحة الرئيسية
]

# عرض ملفات الوسائط (Media) أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
