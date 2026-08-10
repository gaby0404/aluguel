from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Usuario
from .models import Imovel
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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






@api_view(['GET', 'POST'])
def listar_imoveis(request):
    if request.method == 'GET':
         queryset = Imovel.objects.all().order_by('username')
         serializers = ImovelSerializers(queryset, many=True)
         return Response(serializers.data)
    elif request.method == 'POST':
         serializers = ImovelSerializers(data = request.data)
         if serializers.is_valid():
              serializers.save()
              return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


class ImovelAPIView(APIView):
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