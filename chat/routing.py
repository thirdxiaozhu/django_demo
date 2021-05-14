# mysite/chat/routing.py

from django.urls import re_path, path
from . import consumers
#要在类的后面加上.as_asgi()!!!!!!!!!!!!!!!!!!!!!!!!!
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    path("ws/push/<room_name>", consumers.PushMessage.as_asgi()),
]