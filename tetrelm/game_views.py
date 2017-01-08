from django.http import HttpResponse
from .models import Game
from django.core import serializers

def index(req):
    games = Game.objects.all()
    data = seriaizers.serialize("json", games)
    return HttpResponse(data)

def create(req):
    game = Game()
    game.save()
    return HttpResponse(game.id)

def show(req, game_id):
    games = Game.objects.filter(pk=game_id)
    data = serializers.serialize("json", games)
    return HttpResponse(data)
