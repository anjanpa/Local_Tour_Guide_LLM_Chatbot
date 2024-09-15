"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
import chatbot.routing as ch
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


django_application = get_asgi_application()

application=ProtocolTypeRouter({
    'http':django_application,
    "websocket":URLRouter(ch.websocket_urlpatterns)
})

