from django.contrib.auth.models import User, Group
from rest_framework import serializers
import json
from .models import Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Player
        fields = [ 'player_id','username', 'xp', 'gold']

