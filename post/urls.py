from django.urls import path, include
from .apps import PostConfig

from rest_framework.routers import DefaultRouter
from .views import PostViewSet


app_name = PostConfig.name

router = DefaultRouter()
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
