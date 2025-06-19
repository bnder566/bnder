from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

IS_SELLER_CHOICES = (
    (True, 'نعم'),
    (False, 'لا'),
)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='كلمة المرور',
        min_length=8,
        help_text='يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل.'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='تأكيد كلمة المرور'
    )
    phone_number = forms.CharField(
        label='رقم الجوال',
        max_length=10,
        help_text='يجب أن يبدأ بـ 05 ويتكون من 10 خانات.'
    )
    is_seller = forms.ChoiceField(
        label='هل أنت بائع؟',
        choices=IS_SELLER_CHOICES,
        widget=forms.RadioSelect,
        initial=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()

        # التحقق من تطابق كلمتي المرور
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "❌ كلمتا المرور غير متطابقتين.")

        # التحقق من صحة رقم الجوال
        phone = cleaned_data.get('phone_number')
        if phone:
            if not phone.startswith('05') or not phone.isdigit() or len(phone) != 10:
                self.add_error('phone_number', "❌ رقم الجوال غير صحيح. يجب أن يبدأ بـ 05 ويتكون من 10 خانات رقمية.")

        return cleaned_data
