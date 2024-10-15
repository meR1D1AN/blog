from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API приложение для написания постов и комментирования их",
        default_version="v1.01",
        contact=openapi.Contact(email="nikita@mer1d1an.ru"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls"), name="users"),
    path("posts/", include("post.urls"), name="posts"),
    path("comments/", include("comment.urls"), name="comments"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
