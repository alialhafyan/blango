from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views as auth_views
from blog.api.views import PostList, PostDetail, UserDetail
import os

# تعريف schema_view
schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # لضمان وصول الجميع إلى الوثائق
)

# تعريف urlpatterns
urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>/", UserDetail.as_view(), name="api_user_detail"),
    
    # مصادقة REST framework
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", auth_views.obtain_auth_token),

    # مسارات swagger
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
