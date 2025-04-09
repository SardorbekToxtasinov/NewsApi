from django.urls import path, include  # path va include funktsiyalarini import qilamiz

urlpatterns = [
    # User API uchun URL-larni qo‘shamiz
    path('', include('api.urls.user')),  # 'api.urls.user' modulidagi URL-larni qo‘shamiz
    
    # Category API uchun URL-larni qo‘shamiz
    path('', include('api.urls.category')),  # 'api.urls.category' modulidagi URL-larni qo‘shamiz
    
    # Comment API uchun URL-larni qo‘shamiz
    path('', include('api.urls.comment')),  # 'api.urls.comment' modulidagi URL-larni qo‘shamiz
    
    # New (Yangiliklar) API uchun URL-larni qo‘shamiz
    path('', include('api.urls.new')),  # 'api.urls.new' modulidagi URL-larni qo‘shamiz
    
    # Bookmark API uchun URL-larni qo‘shamiz
    path('', include('api.urls.bookmark')),  # 'api.urls.bookmark' modulidagi URL-larni qo‘shamiz
]
