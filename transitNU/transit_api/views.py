from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Train
from .serializers import TrainSerializer

class TrainList(APIView):  
    permission_classes = [permissions.AllowAny]
    serializer_class = TrainSerializer
    http_method_names = ['get']

    def get(self, request):
        trains = Train.objects.all()
        serializer = TrainSerializer(trains, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)