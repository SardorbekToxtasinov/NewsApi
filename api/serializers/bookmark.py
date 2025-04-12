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
        fields = ['id', 'news', 'user','new_title']  # Qaytariladigan maydonlar ro'yxati
        read_only_fields = ['user', 'created_at']  # 'user' va 'created_at' maydonlari faqat o'qish uchun

    # Modelni qanday ko'rinishda qaytarishni belgilash
    def to_representation(self, instance):
        try:
            data = super().to_representation(instance)
            
            # 'created_at' maydonini kerakli formatda qaytarish
            data["created_at"] = instance.created_at.strftime("%Y-%m-%d %H:%M")
            
            # Agar foydalanuvchi mavjud bo'lsa, uning ma'lumotlarini qo'shish
            if instance.user:
                data['user'] = UserSerializer(instance.user).data

            return data
        except AttributeError as e:
            # Handle the case where 'created_at' is missing or 'instance' is not a model object
            return {"error": "Error with data representation: Missing 'created_at' or incorrect instance."}
