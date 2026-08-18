from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_viewset import *

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'imoveis', ImovelViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'pagamentos', PagamentoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
