from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def listar_usuarios(request):
    if request.method == 'GET':
         queryset = Usuario.objects.all().order_by('username')
         serializers = UsuarioSerializers(queryset, many=True)
         return Response(serializers.data)
    elif request.method == 'POST':
         serializers = UsuarioSerializers(data = request.data)
         if serializers.is_valid():
              serializers.save()
              return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


class UsuarioAPIView(APIView):
     def get(self, request):
          usuarios = Usuario.objects.all()
          serializers = UsuarioSerializers(usuarios, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = UsuarioSerializers(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetailAPIView(APIView):
     def get_object(self, pk):
          return Usuario.objects.get(pk=pk)

     def get(self, request, pk):
          usuario = self.get_object(pk)
          serializers = UsuarioSerializers(usuario)
          return Response(serializers.data)

     def put(self, request, pk):
          usuario = self.get_object(pk)
          serializers = UsuarioSerializers(usuario, data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_200_OK)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
          usuario = self.get_object(pk)
          usuario.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)



class ImovelAPIView(APIView):
     # permission_classes = [IsAuthenticated]
     def get(self, request):
          imovel = Imovel.objects.all()
          serializers = ImovelSerializers(imovel, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = ImovelSerializers(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ImovelDetailAPIView(APIView):
     def get_object(self, pk):
          return Imovel.objects.get(pk=pk)

     def get(self, request, pk):
          imovel = self.get_object(pk)
          serializers = ImovelSerializers(imovel)
          return Response(serializers.data)

     def put(self, request, pk):
          imovel = self.get_object(pk)
          serializers = ImovelSerializers(imovel, data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_200_OK)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
          imovel = self.get_object(pk)
          imovel.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)




class ContratoAPIView(APIView):
     def get(self, request):
          contrato = Contrato.objects.all()
          serializers = ContratoSerializers(contrato, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = ContratoSerializers(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ContratoDetailAPIView(APIView):
     def get_object(self, pk):
          return Contrato.objects.get(pk=pk)

     def get(self, request, pk):
          contrato = self.get_object(pk)
          serializers = ContratoSerializers(contrato)
          return Response(serializers.data)

     def put(self, request, pk):
          contrato = self.get_object(pk)
          serializers = ContratoSerializers(contrato, data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_200_OK)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
          contrato = self.get_object(pk)
          contrato.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)




class PagamentoAPIView(APIView):
     # permission_classes = [IsAuthenticated]
     def get(self, request):
          pagamento = Pagamento.objects.all()
          serializers = PagamentoSerializers(pagamento, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = PagamentoSerializers(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class PagamentoDetailAPIView(APIView):
     def get_object(self, pk):
          return Pagamento.objects.get(pk=pk)

     def get(self, request, pk):
          pagamento = self.get_object(pk)
          serializers = PagamentoSerializers(pagamento)
          return Response(serializers.data)

     def put(self, request, pk):
          pagamento = self.get_object(pk)
          serializers = PagamentoSerializers(pagamento, data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_200_OK)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
          pagamento = self.get_object(pk)
          pagamento.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)