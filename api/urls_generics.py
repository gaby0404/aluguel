from rest_framework.urls import path
from .views_generics import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('usuarios', UsuarioListCreateGeneric.as_view()),
    path('usuario/<int:pk>', UsuarioUpdateDestroyGeneric.as_view()),

    path('imoveis', ImovelListCreateGeneric.as_view()),
    path('imovel/<int:pk>', ImovelUpdateDelete.as_view()),

    path('pagamento', PagamentoListCreateGeneric.as_view()),
    path('pagamento/<int:pk>', PagamentoUpdateDelete.as_view()),

    path('contrato', ContratoListCreateGeneric.as_view()),
    path('pagamento/<int:pk>', ContratoUpdateDelete.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
] 



