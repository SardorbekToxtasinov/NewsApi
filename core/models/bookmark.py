# Django modeli va kerakli modullarni import qilamiz
from django.db import models
from django.contrib.auth.models import User  # Foydalanuvchi modelini import qilamiz
from core.models.new import *  # Yangiliklar modelini import qilamiz (core app ichidan)

# Bookmark modeli - foydalanuvchi tomonidan saqlangan yangiliklarni belgilash
class Bookmark(models.Model):
    # Foydalanuvchi va yangilik o'rtasida foreign key o'rnatiladi
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')  
    # Yangilik va foydalanuvchi o'rtasida foreign key o'rnatiladi
    news = models.ForeignKey(New, on_delete=models.CASCADE, related_name='bookmarked_by')
    # Saqlangan vaqt (yangilik saqlangan paytni belgilaydi)
    created_at = models.DateTimeField(auto_now_add=True)

    # Meta klassi yordamida user va news o'rtasida birga bo'lishi kerak bo'lgan noyob juftlikni o'rnatamiz
    class Meta:
        unique_together = ('user', 'news')  # Foydalanuvchi va yangilik bo'yicha noyob bo'lishini ta'minlaymiz

    # Modelning string ko'rinishini qaytarish
    def __str__(self):
        return f'{self.user.username} saved {self.news.title}'  # Foydalanuvchi va yangilik nomini qaytaradi
