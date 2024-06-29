from django.urls import path
from .views import ArticlesList, ArticlesDetail, ArticlesList, ArticlesDetail

from django.conf import settings
from django.conf.urls.static import static

# from .views import UserViewSet, ArViewSet
# from rest_framework.routers import SimpleRouter

urlpatterns = [
    path("<int:pk>/", ArticlesDetail.as_view(), name="post_detail"),
    path("", ArticlesList.as_view(), name="post_list"),
    path("users/", ArticlesList.as_view()),
    path("users/<int:pk>/", ArticlesDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)