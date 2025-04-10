# Django modeli va kerakli modullarni import qilamiz
from django.db import models
from django.contrib.auth.models import User  # Foydalanuvchi modelini import qilamiz
from .category import *  # Kategoriya modelini import qilamiz (bu model boshqa faylga joylashtirilgan)

# New modeli - Yangiliklarni saqlash uchun
class New(models.Model):
    # Yangilikning sarlavhasi (maksimal uzunlik 255 ta belgidan iborat)
    title = models.CharField(max_length=255)  
    # Yangilikning matni
    content = models.TextField()  
    # Yangilik rasmi (rasm fayli bo'lsa, upload qilish uchun joy ajratiladi)
    image = models.ImageField(upload_to='news-img', blank=True, null=True)  # Rasm bo'lmasa, bo'sh qoldirish mumkin
    # Yangilik kategoriyasi (foreign key, kategoriya o'zgarishi yangilikka ta'sir qilmaydi)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')  
    # Yangilik muallifi (foreign key, foydalanuvchi o'chirilsa, null bo'ladi)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author')
    # Yangilik yaratilgan vaqt
    created_at = models.DateTimeField(auto_now_add=True)  # Har safar yangilik yaratilganda avtomatik ravishda vaqtni saqlaydi
    # Yangilik yangilangan vaqt
    updated_at = models.DateTimeField(auto_now=True)  # Har safar yangilik yangilanganida avtomatik ravishda vaqtni saqlaydi
    # Yangilikka kirishlar soni (ijobiy butun son)
    view = models.PositiveIntegerField(default=0)  # Dastlabki qiymat 0 deb belgilangan

    # Modelning string ko'rinishini qaytarish
    def __str__(self):
        return self.title  # Yangilik sarlavhasini qaytaradi

    class Meta:
        ordering = ["-id"]