# Django Rest Framework routerini import qilamiz
from rest_framework.routers import DefaultRouter
from api.views.comment import *  # Comment API view'larini import qilamiz

# DefaultRouter obyektini yaratamiz
router = DefaultRouter()

# 'comment' endpointini va unga mos keladigan viewsetni ro'yxatdan o'tkazamiz
router.register('comment', CommentViewSet)

# URL'lar ro'yxatini olish
urlpatterns = router.urls  # Router orqali barcha URL'larni qaytarish
