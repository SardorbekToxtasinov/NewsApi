# Django Rest Framework'dan kerakli importlarni qilamiz
from rest_framework.viewsets import ModelViewSet  # ModelViewSetni import qilamiz
from rest_framework import permissions  # Xavfsizlik ruxsatlarini import qilamiz
from core.models.bookmark import *  # Bookmark modelini import qilamiz
from api.serializers.bookmark import *  # Bookmark serializatorini import qilamiz

# Faqat 'Super Admin' va 'server' foydalanuvchilarga ruxsat beradigan maxsus permission sinfi
class IsServerOrSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Agar foydalanuvchi superadmin bo'lsa yoki username 'server' bo'lsa, ruxsat beriladi
        if request.user.is_superuser or request.user.username == 'server':
            return True
        return False

# Bookmark viewset'i - bu modelga oid barcha CRUD amallarini bajarish uchun ishlatiladi
class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()  # Barcha bookmark'larni olish
    serializer_class = BookmarkSerializer  # Serializator sifatida BookmarkSerializer ishlatiladi
    permission_classes = [IsServerOrSuperAdmin]  # Faqat maxsus ruxsatga ega foydalanuvchilar uchun

    # Yangilikni yaratishdan oldin, foydalanuvchining identifikatorini qo'shish
    def perform_create(self, serializer):
        # Foydalanuvchini saqlashda unga tegishli bookmark qo'shish
        serializer.save(user=self.request.user)
