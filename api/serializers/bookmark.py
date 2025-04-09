# Django Rest Framework serializatorlarini import qilamiz
from rest_framework import serializers
from core.models.bookmark import Bookmark  # Bookmark modelini import qilamiz
from core.models.new import *  # Yangiliklar modelini import qilamiz
from api.serializers.user import *  # Foydalanuvchi serializatorini import qilamiz

# Bookmark modelining serializatori - Foydalanuvchi tomonidan saqlangan yangiliklarni qaytarish
class BookmarkSerializer(serializers.ModelSerializer):
    # Yangilikning sarlavhasini (new_title) qaytarish uchun yangi maydon yaratamiz
    new_title = serializers.CharField(source='news.title', read_only=True)  # news.title - yangilik sarlavhasini oladi

    class Meta:
        model = Bookmark  # Bookmark modelidan foydalanamiz
        fields = ['id', 'news', 'user', 'created_at', 'new_title']  # Qaytariladigan maydonlar ro'yxati
        read_only_fields = ['user', 'created_at']  # 'user' va 'created_at' maydonlari faqat o'qish uchun

    # Modelni qanday ko'rinishda qaytarishni belgilash
    def to_representation(self, instance):
        data = super().to_representation(instance)  # Asl serializatsiyani olish
        if instance.user:  # Agar foydalanuvchi mavjud bo'lsa
            data['user'] = UserSerializer(instance.user).data  # Foydalanuvchining serializatsiyasini qo'shish
        return data  # Qaytarilgan ma'lumotni qaytarish
