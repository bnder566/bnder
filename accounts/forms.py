from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='كلمة المرور'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='تأكيد كلمة المرور'
    )
    phone_number = forms.CharField(
        label='رقم الجوال',
        max_length=15
    )
    is_seller = forms.BooleanField(
        required=False,
        label='هل أنت بائع؟'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "❌ كلمتا المرور غير متطابقتين.")

class LoginForm(forms.Form):
    username = forms.CharField(
        label='اسم المستخدم',
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'اسم المستخدم'})
    )
    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'placeholder': 'كلمة المرور'})
    )
