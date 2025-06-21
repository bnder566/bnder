from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Car(models.Model):
    BRAND_CHOICES = [
        ('تويوتا', 'تويوتا'),
        ('هيونداي', 'هيونداي'),
        ('نيسان', 'نيسان'),
        ('أخرى', 'أخرى'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المالك")
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name="العلامة التجارية")
    model = models.CharField(max_length=50, verbose_name="الطراز")
    year = models.PositiveIntegerField(verbose_name="سنة الصنع")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    is_available = models.BooleanField(default=True, verbose_name="متوفر")
    image = CloudinaryField(blank=True, null=True, verbose_name="صورة السيارة")


    class Meta:
        verbose_name = "سيارة"
        verbose_name_plural = "السيارات"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
