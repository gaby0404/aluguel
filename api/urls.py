from rest_framework.urls import path
from .views import *

urlpatterns = [
    path('usuarios', UsuarioAPIView.as_view()),
    path('usuario/<int:pk>', UsuarioDetailAPIView.as_view())
] 
