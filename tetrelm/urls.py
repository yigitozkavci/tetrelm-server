from django.conf.urls import include, url

from . import views
from . import game_views
from . import move_views

moves_extra = [
    url(r'create', move_views.create),
    url(r'(?P<move_id>[0-9]+)', move_views.show),
    url(r'^$', move_views.index),
]

games_extra = [
    url(r'(?P<game_id>[0-9]+)/moves/', include(moves_extra)),
    url(r'(?P<game_id>[0-9]+)', game_views.show),
    url(r'create$', game_views.create),
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/', include(games_extra)),
]
