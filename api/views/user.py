from rest_framework.mixins import CreateModelMixin  # CreateModelMixin ni import qilamiz, bu mixin obyektni yaratish imkonini beradi
from rest_framework.viewsets import GenericViewSet  # GenericViewSet import qilamiz, bu barcha CRUD operatsiyalarini boshqaradi
from django.contrib.auth.models import User  # Django ning User modelini import qilamiz
from rest_framework.permissions import AllowAny  # Har kimga ruxsat berish uchun permission
from api.serializers.user import *  # User modelining serializatorini import qilamiz

# Foydalanuvchini ro‘yxatdan o‘tkazish uchun view
class RegisterUser(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()  # User modelining barcha obyektlari
    permission_classes = [AllowAny]  # Foydalanuvchi ro‘yxatdan o‘tkazishga umumiy ruxsat
    serializer_class = UserSerializer  # User modelining serializatorini ishlatamiz

    def perform_create(self, serializer):
        # Foydalanuvchi yaratishdan oldin parolni alohida saqlash va uni shifrlash
        password = self.request.data.pop("password")  # Parolni so‘rovdan olib tashlaymiz
        user = serializer.save()  # Foydalanuvchini saqlaymiz
        user.set_password(password)  # Parolni shifrlaymiz
        user.save()  # Foydalanuvchini saqlaymiz
