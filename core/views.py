from django.shortcuts import render, redirect
from .forms import ContactForm
from inventory.models import Car  # تأكد من مسار الاستيراد حسب موقع نموذج Car

# الصفحة الرئيسية
def index(request):
    return render(request, 'index.html')

# صفحة اتصل بنا
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# رسالة النجاح بعد الإرسال
def contact_success(request):
    return render(request, 'contact_success.html')

# عرض قائمة السيارات
def cars_list_view(request):
    cars = Car.objects.all()
    return render(request, 'core/cars_list.html', {'cars': cars})
