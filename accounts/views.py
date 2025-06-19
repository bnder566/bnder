from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

from .forms import UserRegistrationForm
from .models import UserProfile


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']

            # تحقق من وجود المستخدم مسبقًا
            if User.objects.filter(username=username).exists():
                messages.error(request, "❌ اسم المستخدم مستخدم بالفعل، الرجاء اختيار اسم آخر.")
            else:
                # إنشاء المستخدم
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()

                # إنشاء الملف الشخصي
                UserProfile.objects.create(
                    user=user,
                    phone_number=form.cleaned_data['phone_number'],
                    is_seller=form.cleaned_data['is_seller']
                )

                messages.success(request, "✅ تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
                return redirect('/accounts/login/')
        else:
            messages.error(request, "❌ تحقق من صحة الحقول المدخلة.")
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    return render(request, 'accounts/login.html')


def check_username_availability(request):
    username = request.GET.get('username', '')
    exists = User.objects.filter(username=username).exists()
    return JsonResponse({'available': not exists})
