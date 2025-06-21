from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from inventory.models import Car  # تأكد أن هذا المسار صحيح

# الصفحة الرئيسية - تعرض السيارات المتوفرة
def index(request):
    cars = Car.objects.filter(is_available=True).order_by('-year', '-id')
    return render(request, 'index.html', {'cars': cars})

# صفحة اتصل بنا
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:contact_success')  # باستخدام namespace
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# صفحة نجاح إرسال النموذج
def contact_success(request):
    return render(request, 'contact_success.html')

# صفحة مستقلة لقائمة السيارات (إن احتجت عرضها خارج الصفحة الرئيسية)
def cars_list_view(request):
    cars = Car.objects.filter(is_available=True).order_by('-year', '-id')
    return render(request, 'core/cars_list.html', {'cars': cars})
