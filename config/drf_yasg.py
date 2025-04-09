# Django Rest Frameworkning 'permissions' modulidan kerakli huquqlarni import qilamiz
from rest_framework import permissions

# drf_yasg modulidan API hujjatlarini yaratish uchun kerakli funksiyalarni import qilamiz
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# get_schema_view funksiyasi yordamida API hujjatlarining asosiy ko'rinishini yaratamiz
schema_view = get_schema_view(
    openapi.Info(
        # API haqidagi ma'lumotlarni belgilaymiz
        title="News API",  # API nomi
        default_version="v1",  # API versiyasi
        description="Test description",  # API tavsifi
        terms_of_service="https://www.google.com/policies/terms/",  # Foydalanish shartlari URL manzili
        contact=openapi.Contact(email="sardorbektoxtasinov28@gmail.com"),  # Kontakt email manzili
        license=openapi.License(name="BSD License"),  # Litsenziya nomi
    ),
    public=True,  # Hujjatlarni umumiy qilish (ya'ni, barcha foydalanuvchilarga ochiq)
    # API uchun ruxsatlar. Bu holatda barcha foydalanuvchilarga ruxsat beriladi (umumiy foydalanish)
    permission_classes=(permissions.AllowAny,),
)
