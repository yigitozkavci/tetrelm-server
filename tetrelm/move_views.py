from django.http import HttpResponse
from .models import Game, Move
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

def index(req, game_id):
    game = Game.objects.get(pk=game_id)
    moves = game.move_set.all()
    data = serializers.serialize("json", moves)
    return HttpResponse(data)

@csrf_exempt
def create(req, game_id):
    game = Game.objects.get(pk=game_id)
    move_data = json.loads(req.body)
    print(move_data)
    move = game.move_set.create(
        selected_piece=move_data['selected_piece'],
        board=move_data['board'],
    )
    move.generate_x_position()
    move.save()
    data = {
        "x_position": move.x_position
    }
    return HttpResponse(json.dumps(data))

def show(req, game_id, move_id):
    game = Game.objects.get(pk=game_id)
    moves = game.move_set.filter(pk=move_id)
    data = serializers.serialize("json", moves)
    return HttpResponse(data)
