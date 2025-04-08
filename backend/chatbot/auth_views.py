from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "Logged in successfully"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    return Response({"error": "Signup not implemented yet"}, status=status.HTTP_501_NOT_IMPLEMENTED)

@api_view(['POST'])
@permission_classes([AllowAny])
def signout(request):
    logout(request)
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
