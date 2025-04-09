# Django Rest Framework serializatorlarini import qilamiz
from rest_framework import serializers
from django.contrib.auth.models import User  # Django'dagi foydalanuvchi modelini import qilamiz

# User modelining serializatori - Foydalanuvchi ma'lumotlarini JSON formatida qaytarish
class UserSerializer(serializers.ModelSerializer):
    # Foydalanuvchining parol maydoni faqat yozish uchun (write_only)
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User  # User modelidan foydalanamiz
        fields = ('id', 'username', 'email', 'password')  # Foydalanuvchi uchun kerakli maydonlar ro'yxati
