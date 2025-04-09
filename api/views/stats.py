from rest_framework.generics import ListAPIView  # ListAPIView import qilamiz
from core.models.new import New  # New modelini import qilamiz
from api.serializers.new import *  # New serializatorini import qilamiz

# Yangi yangiliklar ro‘yxati (eng so‘nggi yangiliklar)
class RecentNew(ListAPIView):
    queryset = New.objects.order_by('-created_at')[:10]  # So‘nggi 10 yangilikni tartiblangan holda olamiz
    serializer_class = NewSerializer  # Yangiliklar uchun serializator

# Eng yuqori yangiliklar (eng so‘nggi 5 yangilik)
class Top5New(ListAPIView):
    queryset = New.objects.order_by('-created_at')[:5]  # So‘nggi 5 yangilikni olish
    serializer_class = NewSerializer  # Yangiliklar uchun serializator

# Eng ko‘p ko‘rilgan yangiliklar
class MostView(ListAPIView):
    queryset = New.objects.order_by('-view')  # Ko‘rishlar soni bo‘yicha saralangan yangiliklar
    serializer_class = NewSerializer  # Yangiliklar uchun serializator
