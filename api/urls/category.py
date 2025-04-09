# Django Rest Framework routerini import qilamiz
from rest_framework.routers import DefaultRouter
from api.views.category import *  # Category API view'larini import qilamiz

# DefaultRouter obyektini yaratamiz
router = DefaultRouter()

# 'category' endpointini va unga mos keladigan viewsetni ro'yxatdan o'tkazamiz
router.register('category', CategoryViewSet)

# URL'lar ro'yxatini olish
urlpatterns = router.urls  # Router orqali barcha URL'larni qaytarish
