"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import csrf_exempt  # Add this import
from django.conf import settings
from django.conf.urls.static import static

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

# Plain Django views, no DRF decorators
@csrf_exempt  # Optional, ensures GET works without CSRF issues
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

# Serve static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
