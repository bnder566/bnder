from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان (سري)
SECRET_KEY = 'django-insecure-!xz7&apjfy+h3110hp4hvev=i9wr@dodj0h@p+b2lggiim*urc'

# وضع التطوير
DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات خارجية
    'cloudinary',
    'cloudinary_storage',

    # التطبيقات المخصصة للمشروع
    'accounts',   # إدارة المستخدمين وتسجيل الدخول
    'inventory',  # إدارة بيانات السيارات
    'core',       # الصفحات العامة والواجهة الرئيسية
]

# الميدل وير
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف الروابط الرئيسي
ROOT_URLCONF = 'yoyo.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# تطبيق WSGI
WSGI_APPLICATION = 'yoyo.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = 'static/'

# ملفات الميديا - Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dj8rmgbo4',
    'API_KEY': '574838334652811',
    'API_SECRET': '0VONXvC0Nixye7yuDP2Aud5-VAY',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# الإعداد الافتراضي لحقل الـ ID
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import cloudinary

cloudinary.config( 
  cloud_name = 'dj8rmgbo4', 
  api_key = '574838334652811', 
  api_secret = '0VONXvC0Nixye7yuDP2Aud5-VAY' 
)
