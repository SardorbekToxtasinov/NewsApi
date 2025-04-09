# Django modeli va kerakli modullarni import qilamiz
from django.db import models

# Category modeli - Yangilik kategoriyalarini saqlash uchun
class Category(models.Model):
    # Kategoriyaning nomini saqlash uchun max 100 ta belgidan iborat bo'lgan unique (takrorlanmas) matn maydoni
    name = models.CharField(max_length=100, unique=True)

    # Meta klassi yordamida modelga oid qo'shimcha sozlamalar
    class Meta:
        verbose_name_plural = 'Categories'  # Kategoriyalar ro'yxati uchun ko'rsatiladigan nom (ko'plikda)
        verbose_name = 'Category'  # Yagona kategoriya uchun ko'rsatiladigan nom (bitta)

    # Modelning string ko'rinishini qaytarish
    def __str__(self):
        return self.name  # Kategoriyaning nomini qaytaradi
