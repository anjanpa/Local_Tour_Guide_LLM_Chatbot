from channels.consumer import SyncConsumer
import json
from .views.view_context_search import search_context
from .views.view_gqa import generate_response

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.send({"type": "websocket.accept"})

    def websocket_receive(self,event):
        print("Client message received:",event)
        text=event.get('text')
        text=json.loads(text)
        msg=text['msg'] 
        reply=search_context(msg)
        response=generate_response(f"Context: {reply[0]} Question:{msg}")
        try:
            self.send({
                "type": "websocket.send",
                "text": f"{response}"
            })
        except:
            print("An error occurred while sending message to client")  
    def websocket_disconnect(self, event):
        raise StopConsumer()
