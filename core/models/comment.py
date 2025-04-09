# Django modeli va kerakli modullarni import qilamiz
from django.db import models
from django.contrib.auth.models import User  # Foydalanuvchi modelini import qilamiz
from .new import *  # Yangiliklar modelini import qilamiz (bu model boshqa faylga joylashtirilgan)

# Comment modeli - Yangiliklarga izohlar qo'shish
class Comment(models.Model):
    # Yangilik bilan bog'lanish (foreign key - yangilikga izoh qo'shish)
    news = models.ForeignKey(New, on_delete=models.SET_NULL, null=True, related_name='comment_news')  
    # Foydalanuvchi bilan bog'lanish (foreign key - izohni kim yozganligini aniqlash)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment_author')
    # Izoh matni
    text = models.TextField()  
    # Izoh yaratilgan vaqt
    created_at = models.DateTimeField(auto_now_add=True)  # Har safar izoh yaratilganda avtomatik ravishda vaqtni saqlaydi
    
    # Modelning string ko'rinishini qaytarish
    def __str__(self):
        return f'Comment by {self.author} on {self.news.title}'  # Izoh muallifi va yangilik nomini qaytaradi
