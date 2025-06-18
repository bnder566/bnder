from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # روابط التطبيقات
    path('accounts/', include('accounts.urls')),     # حسابات المستخدمين
    path('inventory/', include('inventory.urls')),   # إدارة السيارات
    path('', include('core.urls')),                  # الصفحات العامة (الرئيسية، تواصل، إلخ)
]
