# Django Rest Framework'dan kerakli importlarni qilamiz
from rest_framework.viewsets import ModelViewSet  # ModelViewSetni import qilamiz
from rest_framework import permissions  # Xavfsizlik ruxsatlarini import qilamiz
from core.models.category import *  # Category modelini import qilamiz
from api.serializers.category import *  # Category serializatorini import qilamiz

# Faqat admin yoki superuserlarga ruxsat beradigan maxsus permission sinfi
class IsAdminOrSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Agar foydalanuvchi superuser yoki admin (staff) bo'lsa, ruxsat beriladi
        return request.user.is_superuser or request.user.is_staff

# Category viewset'i - bu modelga oid barcha CRUD amallarini bajarish uchun ishlatiladi
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()  # Barcha category'larni olish
    serializer_class = CategorySerializer  # Serializator sifatida CategorySerializer ishlatiladi

    # Har bir action (xatti-harakat) uchun ruxsatlarni belgilash
    def get_permissions(self):
        # Agar action 'list' (ya'ni, ro'yxatni ko'rish) bo'lsa, barcha foydalanuvchilarga ruxsat
        if self.action == 'list':
            return [permissions.AllowAny()]

        # Agar action 'create', 'update', 'partial_update', yoki 'destroy' bo'lsa, faqat admin yoki superuserga ruxsat
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrSuperuser()]

        # Boshqa holatlarda, barcha foydalanuvchilarga ruxsat
        return [permissions.AllowAny()]
