# Django Rest Framework serializatorlarini import qilamiz
from rest_framework import serializers
from core.models import *  # Core appdagi barcha modellardan foydalanamiz
from api.serializers.user import *  # Foydalanuvchi serializatorini import qilamiz

# Comment modelining serializatori - Yangiliklarga qo'shilgan izohlarni JSON formatida qaytarish
class CommentSerializer(serializers.ModelSerializer):
    # Yangilik sarlavhasini (news_title) alohida maydon sifatida ko'rsatish
    news_title = serializers.CharField(source='news.title', read_only=True)  # news.title - yangilik sarlavhasini oladi

    class Meta:
        model = Comment  # Comment modelidan foydalanamiz
        fields = '__all__'  # Modeldagi barcha maydonlarni serializatsiya qilish
        read_only_fields = ['author', 'created_at']  # 'author' va 'created_at' maydonlari faqat o'qish uchun

    # Modelni qanday ko'rinishda qaytarishni belgilash
    def to_representation(self, instance):
        data = super().to_representation(instance)  # Asl serializatsiyani olish
        if instance.author:  # Agar muallif (foydalanuvchi) mavjud bo'lsa
            data['author'] = UserSerializer(instance.author).data  # Foydalanuvchining serializatsiyasini qo'shish
        return data  # Qaytarilgan ma'lumotni qaytarish
