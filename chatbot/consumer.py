from channels.consumer import AsyncConsumer
import json
from .views.view_context_search import search_context,search_in_vectordb_cosine
from .views.view_intent_search import search_intent
from .views.view_gqa import generate_response

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self,event):
        # print("Client message received:",event)
        text=event.get('text')
        text=json.loads(text)
        msg=text['msg'] 
        print("Client message")
        reply=search_context(msg)
        # intents=search_intent(msg)
        response=generate_response(f"Context: {reply[0]} Question:{msg}")
        try:
            await self.send({
                "type": "websocket.send",
                "text":json.dumps({
                    "response":response
                })
            })
        except:
            print("An error occurred while sending message to client")  
    
    async def websocket_disconnect(self, event):
        print("Connection stopped")