from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import  status
from rest_framework.response import Response
from .models import *
from .serializers import *


class CakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Cakes.objects.all().order_by('pk')
    serializer_class = CakeSerializer  # Сериализатор для модели

    def list(self, request):
        queryset = Cakes.objects.all()
        serializer = CakeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cakes.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CakeSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try: 
            cake = Cakes.objects.get(pk=pk) 
        except Cakes.DoesNotExist: 
            return Response({'message': 'The cake does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        serializer = CakeSerializer(cake, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        return super(CakeViewSet, self).destroy(request, pk)

        try:
            cake = Cake.objects.get(pk=pk)
        except Cake.DoesNotExist: 
            return Response({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        cake.delete()
        return Response({'message': ' Successfully deleted'}, status=status.HTTP_200_OK)

class TasteViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Tastes.objects.all().order_by('pk')
    serializer_class = TasteSerializer  # Сериализатор для модели

    def list(self, request):
        queryset = Tastes.objects.all()
        serializer = TasteSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tastes.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TasteSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try: 
            customer = Tastes.objects.get(pk=pk) 
        except Tastes.DoesNotExist: 
            return Response({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        serializer = TasteSerializer(customer, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 