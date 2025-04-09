# Django Rest Framework routerini import qilamiz
from rest_framework.routers import DefaultRouter
from api.views.user import *  # User API view'larini import qilamiz

# DefaultRouter obyektini yaratamiz
router = DefaultRouter()

# 'user/create' endpointini va unga mos keladigan view'ni ro'yxatdan o'tkazamiz
router.register('user/create', RegisterUser)

# URL'lar ro'yxatini olish
urlpatterns = router.urls  # Router orqali barcha URL'larni qaytarish
