from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):
    
    # def __init__(self, *args, **kwargs): 
    #      super().__init__(*args, **kwargs) 

    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):

        # await self.disconnect()
        pass
    async def receive(self, text_data):
        
        print('>>>>', text_data)

        pass
