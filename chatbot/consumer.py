from channels.consumer import AsyncConsumer
import json
from .views.view_context_search import search_context,search_in_vectordb_cosine
from .views.view_intent_search import search_intent
from .views.view_translation import translate

# from .views.view_eng_to_nep import convert
from .views.view_gqa import generate_response

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self,event):
        # print("Client message received:",event)
        text=event.get('text')
        text=json.loads(text) 
        msg=text['msg'] 
        src_lang=text.get('src_lang','en_XX')
        tgt_lang=text.get('tgt_lang','en_XX')
        print(src_lang,tgt_lang,msg)
        # reply=search_context(msg)
        if src_lang!="en_XX":
            msg=translate(msg,src_lang,tgt_lang='en_XX')
        reply=search_in_vectordb_cosine(msg,5)
        combined_context=[r+' ' for r in reply]
        # intents=search_intent(msg)
        response=generate_response(f"Context: {combined_context} Question:{msg}",tgt_lang=tgt_lang)
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