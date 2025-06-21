from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from .forms import UserRegistrationForm, LoginForm
from .models import UserProfile


# تسجيل مستخدم جديد
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            # التحقق من وجود اسم المستخدم مسبقًا
            if User.objects.filter(username=username).exists():
                messages.error(request, "❌ اسم المستخدم مستخدم بالفعل، الرجاء اختيار اسم آخر.")
            else:
                # إنشاء المستخدم
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()

                # إنشاء الملف الشخصي للمستخدم
                UserProfile.objects.create(
                    user=user,
                    phone_number=form.cleaned_data['phone_number'],
                    is_seller=form.cleaned_data['is_seller'] == 'True'  # تحويل من نص إلى Boolean
                )

                # تسجيل الدخول مباشرة
                user = authenticate(username=username, password=form.cleaned_data['password'])
                if user:
                    login(request, user)
                    messages.success(request, "✅ تم إنشاء الحساب وتسجيل الدخول بنجاح.")
                    return redirect('/')
        else:
            messages.error(request, "❌ تحقق من صحة البيانات المدخلة.")
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


# تسجيل الدخول
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            messages.success(request, "✅ تم تسجيل الدخول بنجاح.")
            return redirect('/')
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة.")
    return render(request, 'accounts/login.html', {'form': form})


# تحقق من توفر اسم المستخدم (AJAX)
def check_username_availability(request):
    username = request.GET.get('username', '')
    exists = User.objects.filter(username=username).exists()
    return JsonResponse({'available': not exists})
