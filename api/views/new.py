# Django Rest Framework'dan kerakli importlarni qilamiz
from rest_framework.viewsets import ModelViewSet  # ModelViewSetni import qilamiz
from rest_framework.response import Response  # Response import qilamiz, ma'lumot yuborish uchun
from django_filters.rest_framework import DjangoFilterBackend  # Filtrlar uchun import
from rest_framework.filters import OrderingFilter  # Saralash uchun import
from rest_framework import permissions  # Ruxsatlarni import
from drf_yasg.utils import swagger_auto_schema  # Swagger hujjatlashtirish uchun import
from drf_yasg import openapi  # Swagger uchun openapi import
import django_filters  # django_filters uchun import
from core.models.new import *  # New modelini import qilamiz
from api.serializers.new import *  # New serializatorini import qilamiz

# Faqat admin va editor guruhidagi foydalanuvchilarga ruxsat beruvchi maxsus permission sinfi
class IsAdminOrEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Foydalanuvchi admin yoki 'editor' guruhida bo'lsa, ruxsat beriladi
        return request.user and (
            request.user.is_staff or request.user.groups.filter(name='editor').exists()
        )

# Yangiliklar uchun filtrlar sinfi: Kategoriyani va muallifni id yoki username bo‘yicha filtrlash
class NewsFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_category', label='Category')  # Kategoriya bo‘yicha filtr
    author = django_filters.CharFilter(method='filter_by_author', label='Author')  # Muallif bo‘yicha filtr

    class Meta:
        model = New
        fields = ['category', 'author']  # Filtrlanadigan maydonlar

    # Kategoriyani id yoki nomi bo‘yicha filtrlash
    def filter_by_category(self, queryset, name, value):
        return queryset.filter(
            models.Q(category__id__iexact=value) |  # Kategoriyani id bo‘yicha qidirish
            models.Q(category__name__icontains=value)  # Kategoriyani nomi bo‘yicha qidirish
        )

    # Muallifni id yoki username bo‘yicha filtrlash
    def filter_by_author(self, queryset, name, value):
        return queryset.filter(
            models.Q(author__id__iexact=value) |  # Muallifni id bo‘yicha qidirish
            models.Q(author__username__icontains=value)  # Muallifni username bo‘yicha qidirish
        )

# Yangiliklar uchun asosiy ViewSet
class NewViewSet(ModelViewSet):
    queryset = New.objects.all()  # Yangiliklar ro‘yxati
    serializer_class = NewSerializer  # Yangiliklar uchun serializator
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Filtrlar va saralash
    filterset_class = NewsFilter  # Filtrlar klassi
    ordering_fields = ['view', 'created_at']  # Saralash uchun maydonlar (views va created_at)

    # Swagger hujjatlashtirish uchun qo‘shimcha parametrlar
    @swagger_auto_schema(
        manual_parameters=[  # Swagger uchun qo‘shimcha query parametrlar
            openapi.Parameter('ordering', openapi.IN_QUERY, description="Saralash (view yoki created_at bo‘yicha)", 
                              type=openapi.TYPE_STRING, enum=['-view', '-created_at']),  # Saralash
            openapi.Parameter('category', openapi.IN_QUERY, description="Kategoriya bo‘yicha filtrlash (nom yoki id)", 
                              type=openapi.TYPE_STRING),  # Kategoriyaga qarab filtr
            openapi.Parameter('author', openapi.IN_QUERY, description="Muallif bo‘yicha filtrlash (username yoki id)", 
                              type=openapi.TYPE_STRING)  # Muallifga qarab filtr
        ]
    )
    def list(self, request, *args, **kwargs):
        # Yangiliklar ro‘yxatini qaytarish (filtr va saralash bilan)
        return super().list(request, *args, **kwargs)

    # Yangilik yaratishda avtomatik ravishda foydalanuvchini muallif sifatida qo‘shish
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Yangilikni ko‘rsatishda, ko‘rishlar sonini oshirish
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  # Yangilikni olish
        instance.view += 1  # Ko‘rishlar sonini oshirish
        instance.save(update_fields=['view'])  # Yangilikni saqlash
        return Response(self.get_serializer(instance).data)  # Yangilikni qaytarish

    # Har bir action uchun ruxsatlarni belgilash
    def get_permissions(self):
        # Agar action 'create', 'update', 'partial_update', yoki 'destroy' bo‘lsa, faqat admin yoki editor guruhidagi foydalanuvchilarga ruxsat
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrEditor()]
        # Boshqa holatlarda barcha foydalanuvchilarga ruxsat
        return [permissions.AllowAny()]
