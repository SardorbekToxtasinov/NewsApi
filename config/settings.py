# Projectning asosiy papkasini olish
import dj_database_url
from pathlib import Path
import os
import environ

# Loyihaning asosiy yo'lini aniqlash
BASE_DIR = Path(__file__).resolve().parent.parent

# env fayllarini o'qish uchun `environ` ob'ekti yaratish
env = environ.Env(
    DEBUG=(bool, False)  # DEBUG holatini False deb o'rnatamiz, lekin bu qiymat .env faylida qayta yozilishi mumkin
)

# .env faylini yuklash
environ.Env.read_env(os.path.join(BASE_DIR, '.env.dev'))


# Tezkor boshlash uchun rivojlanish sozlamalari - ishlab chiqish uchun mo'ljallangan, ishlab chiqarish uchun emas
# https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# Maxfiylik uchun secret keyni saqlash zarur
SECRET_KEY = env('SECRET_KEY')

# Ishlab chiqarishda DEBUG holatini yoqmaslik kerak
DEBUG = env('DEBUG')

# Qaysi hostlarga ruxsat berilishini belgilash
ALLOWED_HOSTS = ['newsapi-0na6.onrender.com', 'localhost', '127.0.0.1']


# Dastur ilovalarining ro'yxati
INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin paneli
    'django.contrib.auth',  # Foydalanuvchi autentifikatsiyasi
    'django.contrib.contenttypes',  # Kontent turlari
    'django.contrib.sessions',  # Sessiyalarni boshqarish
    'django.contrib.messages',  # Xabarlar tizimi
    'django.contrib.staticfiles',  # Statik fayllarni qo'llab-quvvatlash
    'core.apps.CoreConfig',  # Core ilovasi
    'rest_framework',  # Django Rest Framework
    'rest_framework_simplejwt',  # JWT autentifikatsiya
    'django_filters',  # Django filtrlash
    'drf_yasg',  # Swagger hujjatlari
]

# Middleware - Xavfsizlik va qo'shimcha tizim funktsiyalari uchun dasturdan o‘tuvchi funksiyalar
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Xavfsizlik
    'django.contrib.sessions.middleware.SessionMiddleware',  # Sessiya boshqaruvi
    'django.middleware.common.CommonMiddleware',  # Oddiy middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF himoyasi
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autentifikatsiya
    'django.contrib.messages.middleware.MessageMiddleware',  # Xabarlar tizimi
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # X-Frame-Options himoyasi
]

# Dastur URL konfiguratsiyasi
ROOT_URLCONF = 'config.urls'

# Template tizimi konfiguratsiyasi
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django templatelari
        'DIRS': [],  # Template fayllar joylashgan papka
        'APP_DIRS': True,  # Ilovalar ichidagi templates papkasidan foydalanish
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # So'rovni ishlov berish
                'django.contrib.auth.context_processors.auth',  # Foydalanuvchi autentifikatsiyasini qo'llash
                'django.contrib.messages.context_processors.messages',  # Xabarlar tizimi
            ],
        },
    },
]

# WSGI (Web Server Gateway Interface) ilovasi
WSGI_APPLICATION = 'config.wsgi.application'

# DATABASE_URL dan foydalanish
DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}

# Parolni tekshirishning asosiy validatsiya qoidalari
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Parol va foydalanuvchi ma'lumotlari o'xshashligini tekshirish
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Parol uzunligini tekshirish
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Oddiy parollarni tekshirish
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Faqat raqamli parollarni taqiqlash
    },
]

# Django Rest Framework sozlamalari
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT autentifikatsiya
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'  # Foydalanuvchilarni autentifikatsiya qilish yoki faqat o'qish huquqi berish
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',  # Django filtrlashni qo'llash
        'rest_framework.filters.OrderingFilter',  # Ordering filtrlashni qo'llash
    ],
}

# Swagger hujjatlari konfiguratsiyasi
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',  # Authorization headerdan foydalanish
            'in': 'Header'  # Headerda yuboriladigan token
        }
    },
}


# Xalqaro tizim sozlamalari
LANGUAGE_CODE = 'uz-uz'  # Tilni o'rnatish (O'zbek tili)

TIME_ZONE = 'Asia/Tashkent'  # Vaqt zonasini o'rnatish

USE_I18N = True  # Xalqaro tizimni faollashtirish

USE_TZ = True  # Vaqt zonasini qo'llash


# Statik fayllar sozlamalari (CSS, JavaScript, rasm fayllari)
STATIC_URL = 'static/'  # Statik fayllar URL manzili

MEDIA_URL = 'media/'  # Media fayllar URL manzili
MEDIA_ROOT = BASE_DIR / 'media'  # Media fayllar joylashgan papka

# Asosiy identifikator (primary key) turini sozlash
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Avtomatik raqamli identifikatorni 'BigAutoField' qilib belgilash
