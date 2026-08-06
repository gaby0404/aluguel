from rest_framework import serializers
from .models import Usuario, Imovel, Pagamento, Contrato

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ImovelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class ContratoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class PagamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
