from django.urls import re_path

from .consumers import ChatConsumer
"""
ws = WebSocket ( Para fazer as comunicações em realtime}
(?P<nome_sala>\w+)/$) = Expressão Regualar ( vai falar que o nome da sala preciasa ter nomes e letras)

"""
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$)', ChatConsumer),
]