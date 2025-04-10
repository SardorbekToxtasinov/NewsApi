from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models.bookmark import Bookmark
from api.serializers.bookmark import BookmarkSerializer

# Bookmark viewset'i - bu modelga oid barcha CRUD amallarini bajarish uchun ishlatiladi
class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all() # Barcha bookmark'larni olish
    serializer_class = BookmarkSerializer  # Serializator sifatida BookmarkSerializer ishlatiladi
    permission_classes = [IsAuthenticated]  # Faqat autentifikatsiyalangan foydalanuvchilarga ruxsat beriladi

    # Faqat foydalanuvchiga tegishli bookmarklarni olish
    def get_queryset(self):
        # Faqat o'ziga tegishli bookmarklar ko'rsatiladi
        return Bookmark.objects.filter(user=self.request.user)

    # Yangilikni yaratishdan oldin, foydalanuvchining identifikatorini qo'shish
    def perform_create(self, serializer):
        # Foydalanuvchini saqlashda unga tegishli bookmark qo'shish
        serializer.save(user=self.request.user)