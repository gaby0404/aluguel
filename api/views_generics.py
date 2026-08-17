from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import *
from .serializers import *

class UsuarioListCreateGeneric(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializers_class = UsuarioSerializers

class UsuarioUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

class ImovelListCreateGeneric(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializers

class ImovelUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializers

class ContratoListCreateGeneric(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializers

class ContratoUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializers

class PagamentoListCreateGeneric(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializers

class PagamentoUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializers