"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import csrf_exempt

schema_view = get_schema_view(
    openapi.Info(
        title="Chatbot API",
        default_version='v1',
        description="API for Chatbot Assistant",
        contact=openapi.Contact(email="badr@example.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

@csrf_exempt
def swagger_redirect(request):
    return schema_view.with_ui('swagger', cache_timeout=0)(request)

@csrf_exempt
def redoc_redirect(request):
    return schema_view.with_ui('redoc', cache_timeout=0)(request)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chatbot.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', swagger_redirect, name='schema-swagger-ui'),
    path('redoc/', redoc_redirect, name='schema-redoc'),
]
