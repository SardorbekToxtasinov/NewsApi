from django.contrib import admin  # Django admin panelini import qilamiz
from django.urls import path, include  # URL-lar uchun path va include funksiyalarini import qilamiz
from django.conf import settings  # Django sozlamalarini import qilamiz
from django.conf.urls.static import static  # Statis fayllarni sozlash uchun import qilamiz
from config.drf_yasg import schema_view  # Swagger hujjatlarini yaratish uchun import qilamiz
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # JWT token olish va yangilash uchun import qilamiz

# Auth (JWT autentifikatsiyasi) uchun URL-lar
auth = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Token olish
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Tokenni yangilash
]

# Swagger va Redoc hujjatlari uchun URL-lar
swagger = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc UI
]

# Boshqa URL-lar
urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin paneli
    path('api/', include('api.main_routers')),  # API-lar uchun URL-larni qo‘shamiz
    path('api-auth/', include('rest_framework.urls'))  # DRF uchun auth URL-lar
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Statik fayllarni qo‘shamiz

urlpatterns += swagger + auth  # Swagger va JWT autentifikatsiya URL-larini oxiriga qo‘shamiz
