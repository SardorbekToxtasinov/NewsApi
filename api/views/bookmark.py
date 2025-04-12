from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models.bookmark import Bookmark
from api.serializers.bookmark import BookmarkSerializer

class BookmarkViewSet(ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Swagger uchun bo'sh queryset
        if getattr(self, 'swagger_fake_view', False):
            return Bookmark.objects.none()
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        news = self.request.data.get('news')

        existing = Bookmark.objects.filter(user=user, news=news).first()
        if existing:
            existing.delete()
            return Response("A")
        else:
            serializer.save(user=user)