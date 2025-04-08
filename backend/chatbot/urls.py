from django.urls import path
from .views import chat, health
from .auth_views import signup, signin, signout

urlpatterns = [
    path('', chat, name='chat'),
    path('health/', health, name='health'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
]
