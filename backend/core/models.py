from django.db import models

"""
Game        = represents a game
Contributor = represent a person/developer
Credit      = links game and contributor with role
"""
class Game(models.Model):
    name = models.CharField(max_length=200)

class Contributor(models.Model):
    name = models.CharField(max_length=200)

class Credit(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        relate_name="credits"
    )
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE,
        related_name="credits"
    )
    role = models.CharField(max_length=100)