# import json

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# from channels.generic.websocket import AsyncWebsocketConsumer

# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# #from asgiref.sync import await_to_sync

# class ChatConsumer(WebsocketConsumer):
#     """ handshake websocket front end """

    
# # async_to_sync (channel_layer.receive) ('test_channel')
#     def connect(self):

#         self.person_name=self.scope['url_route']['kwargs']['person_name']
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 "type":"chat_message",
#                 "message":self.person_name+" Joined Chat"
#             }
#         )
#         self.accept()
#         self.rooms = set()

#     def disconnect(self, code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 "type":"chat_message",
#                 "message":self.person_name+" Left Chat"
#             }
#         )

#         async_to_sync(self.channel_layer.group_discard)(
#                 self.room_group_name,
#                 self.channel_name
#             )

#     # Receive message from WebSocket
#     async def receive(self, text_data=None, bytes_data=None):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
        
#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message':self.person_name+" : "+message   
#             }
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         """ exhange message here """
#         message = event['message']
        

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#             'message': message,
#         }))

import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.person_name=self.scope['url_route']['kwargs']['person_name']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":self.person_name+" Joined Chat"
            }
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":self.person_name+" Left Chat"
            }
        )
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message':self.person_name+" : "+ message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))