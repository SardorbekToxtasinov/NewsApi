# Django Rest Framework routerini import qilamiz
from rest_framework.routers import DefaultRouter
from api.views.bookmark import *  # Bookmark API view'larini import qilamiz

# DefaultRouter obyektini yaratamiz
router = DefaultRouter()

# 'bookmark' endpointini va unga mos keladigan viewsetni ro'yxatdan o'tkazamiz
router.register('bookmark', BookmarkViewSet)

# URL'lar ro'yxatini olish
urlpatterns = router.urls  # Router orqali barcha URL'larni qaytarish
