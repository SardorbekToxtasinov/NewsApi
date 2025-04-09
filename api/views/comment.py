# Django Rest Framework'dan kerakli importlarni qilamiz
from rest_framework.viewsets import ModelViewSet  # ModelViewSetni import qilamiz
from rest_framework import permissions  # Xavfsizlik ruxsatlarini import qilamiz
from core.models.comment import *  # Comment modelini import qilamiz
from api.serializers.comment import *  # Comment serializatorini import qilamiz

# Faqat kommentariyaning egasi yoki adminlarga ruxsat beradigan maxsus permission sinfi
class IsCommentOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Agar foydalanuvchi kommentariyaning egasi yoki admin bo'lsa, ruxsat beriladi
        return request.user == obj.author or request.user.is_superuser

# Comment viewset'i - bu modelga oid barcha CRUD amallarini bajarish uchun ishlatiladi
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()  # Barcha comment'larni olish
    serializer_class = CommentSerializer  # Serializator sifatida CommentSerializer ishlatiladi

    # Yangi comment yaratishda, foydalanuvchining identifikatorini qo'shish
    def perform_create(self, serializer):
        # Foydalanuvchini saqlashda unga tegishli comment qo'shish
        serializer.save(author=self.request.user)

    # Har bir action (xatti-harakat) uchun ruxsatlarni belgilash
    def get_permissions(self):
        # Agar action 'create' bo'lsa, faqat autentifikatsiyalangan foydalanuvchilarga ruxsat
        if self.action == 'create':
            return [permissions.IsAuthenticated()]

        # Agar action 'update', 'partial_update', yoki 'destroy' bo'lsa, faqat kommentariyaning egasi yoki adminlarga ruxsat
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsCommentOwnerOrAdmin()]

        # Boshqa holatlarda, barcha foydalanuvchilarga ruxsat
        return [permissions.AllowAny()]
