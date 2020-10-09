from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

# from channels.routing import ProtocolTypeRouter,URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from chat import consumers

# ws_pattern= [
#     path('ws/chat/<room_name>/<person_name>',consumers.ChatConsumer),
    
# ]

# application= ProtocolTypeRouter(
#     {
#         'websocket':AuthMiddlewareStack(URLRouter(ws_pattern))
#     }
# )