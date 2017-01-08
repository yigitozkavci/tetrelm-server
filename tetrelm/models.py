from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField
import random

# Create your models here.

class Game(models.Model):
    time = models.IntegerField(default=0)

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    board = ArrayField(
        ArrayField(
            models.IntegerField(default=0),
            size=23
        ),
        size=10
    )
    selected_piece = models.IntegerField(default=1)
    x_position = models.IntegerField(default=0)

    def generate_x_position(self):
        # TODO: Generate x position based on self.board and tensorflow data
       self.x_position = random.randint(0, 9) 
