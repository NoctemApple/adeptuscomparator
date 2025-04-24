from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer, CreditSerializer

class GameViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides:
    - GET /api/games/       -> list all games
    - GET /api/games/{id}/  -> retrieve a game
    """

    queryset = Game.objects.all()
    serialzer_class = GameSerializer

    @action(detail=True, url_path="credits")
    def credits(self, request, pk=None):
        """
        GET /api/games/{id}/credits/
        Returns: list of credits (contributor + role)
        """
        game = self.get_object()
        credits = game.credits.all()
        serializer = CreditSerializer(credits, many=True)
        return Response(serializer.data)