# Django Rest Framework serializatorlarini import qilamiz
from rest_framework import serializers
from core.models import *  # Core appdagi barcha modellardan foydalanamiz
from api.serializers.category import *  # Kategoriya serializatorini import qilamiz
from api.serializers.user import *  # Foydalanuvchi serializatorini import qilamiz

# New modelining serializatori - Yangiliklarni JSON formatida qaytarish
class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New  # New modelidan foydalanamiz
        fields = '__all__'  # Modeldagi barcha maydonlarni serializatsiya qilish
        read_only_fields = ('author', 'view', 'created_at', 'updated_at')  # 'author', 'view', 'created_at', 'updated_at' maydonlari faqat o'qish uchun

    # Modelni qanday ko'rinishda qaytarishni belgilash
    def to_representation(self, instance):
        data = super().to_representation(instance)  # Asl serializatsiyani olish
        data['category'] = CategorySerializer(instance.category).data  # Kategoriyaning serializatsiyasini qo'shish
        if instance.author:  # Agar muallif (foydalanuvchi) mavjud bo'lsa
            data['author'] = UserSerializer(instance.author).data  # Foydalanuvchining serializatsiyasini qo'shish
        data['view'] = instance.view  # Yangilikka bo'lgan qarashlar sonini alohida qo'shish
        return data  # Qaytarilgan ma'lumotni qaytarish
