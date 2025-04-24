from rest_framework import serializers
from .models import Game, Credit

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "name"]

class CreditSerializer(serializers.ModelSerializer):
    contributor = serializers.StringRelatedField()

    class Meta:
        model = Credit
        fields = ["contributor", "role"]