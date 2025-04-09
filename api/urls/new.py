# Django URL'larini import qilamiz
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views.new import *  # New API view'larini import qilamiz
from api.views.stats import *  # Stats API view'larini import qilamiz

# DefaultRouter obyektini yaratamiz
router = DefaultRouter()

# 'new' endpointini va unga mos keladigan viewsetni ro'yxatdan o'tkazamiz
router.register('new', NewViewSet)

# Qo'shimcha yo'nalishlar - yangiliklar bo'yicha statistikalarni olish
urlpatterns = [
    path('news/recent/', RecentNew.as_view(), name='recent-news'),  # Yangi yangiliklarni olish
    path('news/top-5/', Top5New.as_view(), name='top-5-news'),  # Eng mashhur 5 yangilikni olish
    path('news/most-viewed/', MostView.as_view(), name='most-viewed-news'),  # Eng ko'p ko'rilgan yangiliklarni olish
]

# DefaultRouter tomonidan yaratilgan URL'larni qo'shish
urlpatterns += router.urls
