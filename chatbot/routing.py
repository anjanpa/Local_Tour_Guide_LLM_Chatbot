from django.urls import path,re_path
from . import consumer

websocket_urlpatterns=[
     re_path(r"ch", consumer.MySyncConsumer.as_asgi()),
]

