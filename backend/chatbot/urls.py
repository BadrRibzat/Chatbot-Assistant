from django.urls import path
from .views import chat
from .auth_views import signup, signin, signout

urlpatterns = [
    path('', chat, name='chat'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
]
