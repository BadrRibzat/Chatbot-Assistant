"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def api_auth_login(request):
    return include('rest_framework.urls')(request)

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

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def swagger_redirect(request):
    return schema_view.with_ui('swagger', cache_timeout=0)(request)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def redoc_redirect(request):
    return schema_view.with_ui('redoc', cache_timeout=0)(request)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chatbot.urls')),
    path('api-auth/login/', api_auth_login, name='api-auth-login'),
    path('api-auth/', include('rest_framework.urls')),
    path('', swagger_redirect, name='schema-swagger-ui'),
    path('redoc/', redoc_redirect, name='schema-redoc'),
]
