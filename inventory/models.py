from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    BRAND_CHOICES = [
        ('تويوتا', 'تويوتا'),
        ('هيونداي', 'هيونداي'),
        ('نيسان', 'نيسان'),
        ('أخرى', 'أخرى'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
