from .serializers import PlayerSerializer
from .models import Player
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from rest_framework.decorators import api_view
from uuid import UUID
import json

# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
#   look_url_kwarg = "id"
    serializer_class = PlayerSerializer
    
    def get_queryset(self):
        print("get_queryset!")
        queryset = Player.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(player_id=UUID(id))
        return queryset

@api_view(['GET'])
def leaderboard(request):
    sortby = request.query_params.get('sortby', "")
    size = request.query_params.get('size', "10")
    queryset = serializers.serialize("json", Player.objects.all().order_by(sortby).reverse()[:int(size)])
    print(queryset)
    return Response(queryset)

#@api_view(['PUT'])
#def update(request):
    
    