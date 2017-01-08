from django.http import HttpResponse

def index(req):
    return HttpResponse("Game Index")

def create(req):
    return HttpResponse("Creating game")
