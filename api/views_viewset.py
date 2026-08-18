from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializers

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializers

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializers