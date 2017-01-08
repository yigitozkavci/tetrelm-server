from django.conf.urls import include, url

from . import views
from . import game_views

games_extra = [
    url(r'create$', game_views.create),
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/', include(games_extra)),
]
