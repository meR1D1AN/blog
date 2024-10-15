from django.urls import path, include
from comment.apps import CommentConfig

from rest_framework.routers import DefaultRouter
from .views import CommentViewSet


app_name = CommentConfig.name

router = DefaultRouter()
router.register(r"", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
