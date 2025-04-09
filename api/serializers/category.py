# Django Rest Framework serializatorlarini import qilamiz
from rest_framework import serializers
from core.models import *  # Core appdagi barcha modellardan foydalanamiz

# Category modelining serializatori - Kategoriyalarni JSON formatida qaytarish
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Category modelidan foydalanamiz
        fields = '__all__'  # Modeldagi barcha maydonlarni serializatsiya qilish
