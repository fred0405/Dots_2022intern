from .serializers import PlayerSerializer
from .models import Player
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from uuid import UUID, uuid4
import json

# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(player_id=UUID(id))
        return queryset

    @api_view(['POST'])
    def CreatePlayer(request):
        try:
            user_name = request.data['username']
            user_id = uuid4()
            new_player = Player(player_id=user_id, username=user_name)
            new_player.save()
            data = {
                "username": user_name, 
                "player_id": str(user_id),
            }
            return JsonResponse(data)
        except:
            return JsonResponse({"error_message":"Some kind of unspecified error has occurred!"}, status=400)
    
    @api_view(['GET', 'PUT'])
    def GetorUpdateInfo(request, player_id):
        try:
            player = Player.objects.get(player_id=player_id)
        except Player.DoesNotExist:
            return JsonResponse({"error_message":"Some kind of unspecified error has occurred!"},status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
#           info = model_to_dict(player)
        #   a = serializers.serialize('json', [player])
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = PlayerSerializer(player, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({"error_message":"Some kind of unspecified error has occurred!"}, status=status.HTTP_400_BAD_REQUEST)  
    
    
    
    @api_view(['GET'])
    def leaderboard(request):
        try:
            sortby = request.query_params.get('sortby', "")
            size = request.query_params.get('size', "10")
            print(sortby, size)
            players = Player.objects.all().order_by('-'+sortby)[0:int(size)].values()
            return Response(players)
        except:
            return JsonResponse({"error_message":"Some kind of unspecified error has occurred!"}, status=status.HTTP_400_BAD_REQUEST)  
#@api_view(['PUT'])
#def update(request):


