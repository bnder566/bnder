from django.shortcuts import render, get_object_or_404
from .models import Car

def cars_list(request):
    """
    عرض قائمة السيارات المتوفرة.
    """
    cars = Car.objects.filter(is_available=True).order_by('-year', '-id')
    return render(request, 'inventory/cars_list.html', {'cars': cars})


def car_detail(request, car_id):
    """
    عرض تفاصيل سيارة محددة بالمعرف car_id.
    يتم تمرير البيانات بشكل صريح للقالب.
    """
    car = get_object_or_404(Car, id=car_id)

    context = {
        'brand': car.brand,
        'model': car.model,
        'year': car.year,
        'price': car.price,
        'owner': car.owner,
        'image': car.image,  # CloudinaryField يحتوي على .url تلقائيًا
        'is_available': car.is_available,
    }

    return render(request, 'inventory/car_detail.html', context)
