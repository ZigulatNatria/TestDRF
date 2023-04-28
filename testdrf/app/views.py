from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Entity
from .serializers import EntitySerializer


# Create your views here.
class EntityAPIVew(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


# class CreateEntityAPI(APIView):
#
#     def post(self, request):
#         serializer = EntitySerializer(data=request.user)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
#         return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)


class CreateEntityAPI(generics.CreateAPIView):
    serializer_class = EntitySerializer

    def user_create(self, serializer):
        serializer.save(modified_by=self.request.user)
