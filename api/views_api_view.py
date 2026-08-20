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
         serializers = UsuarioSerializer(queryset, many=True)
         return Response(serializers.data)
    elif request.method == 'POST':
         serializers = UsuarioSerializer(data = request.data)
         if serializers.is_valid():
              serializers.save()
              return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


class UsuarioAPIView(APIView):
     def get(self, request):
          usuarios = Usuario.objects.all()
          serializers = UsuarioSerializer(usuarios, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = UsuarioSerializer(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetailAPIView(APIView):
     def get_object(self, pk):
          return Usuario.objects.get(pk=pk)

     def get(self, request, pk):
          usuario = self.get_object(pk)
          serializers = UsuarioSerializer(usuario)
          return Response(serializers.data)

     def put(self, request, pk):
          usuario = self.get_object(pk)
          serializers = UsuarioSerializer(usuario, data = request.data)
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
          serializers = ImovelSerializer(imovel, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = ImovelSerializer(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ImovelDetailAPIView(APIView):
     def get_object(self, pk):
          return Imovel.objects.get(pk=pk)

     def get(self, request, pk):
          imovel = self.get_object(pk)
          serializers = ImovelSerializer(imovel)
          return Response(serializers.data)

     def put(self, request, pk):
          imovel = self.get_object(pk)
          serializers = ImovelSerializer(imovel, data = request.data)
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
          serializers = ContratoSerializer(contrato, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = ContratoSerializer(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ContratoDetailAPIView(APIView):
     def get_object(self, pk):
          return Contrato.objects.get(pk=pk)

     def get(self, request, pk):
          contrato = self.get_object(pk)
          serializers = ContratoSerializer(contrato)
          return Response(serializers.data)

     def put(self, request, pk):
          contrato = self.get_object(pk)
          serializers = ContratoSerializer(contrato, data = request.data)
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
          serializers = PagamentoSerializer(pagamento, many=True)
          return Response(serializers.data)

     def post(self, request):
          serializers = PagamentoSerializer(data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_201_CREATED)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class PagamentoDetailAPIView(APIView):
     def get_object(self, pk):
          return Pagamento.objects.get(pk=pk)

     def get(self, request, pk):
          pagamento = self.get_object(pk)
          serializers = PagamentoSerializer(pagamento)
          return Response(serializers.data)

     def put(self, request, pk):
          pagamento = self.get_object(pk)
          serializers = PagamentoSerializer(pagamento, data = request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data, status=status.HTTP_200_OK)
          return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
          pagamento = self.get_object(pk)
          pagamento.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)