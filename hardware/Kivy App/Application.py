"""
This is the Python Kivy Application to house the data from the broker
A trial application is built using the open source Kivy Library
Install Kivy by using pip3/pip install kivy
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
import paho.mqtt.client as mqtt
import time

mqttBroker = "broker.hivemq.com"
client = mqtt.Client("Cylinder Data")
client.connect(mqttBroker)

def on_message(client, userdata, message):
    print("Received: " + str(message.payload.decode("utf-8")))
    
class MainApp(App):
    """def build(self):
        label = Label(
            text='FOULGAS APPLICATION BY APEED',
            size_hint=(.5,.5),
            pos_hint={'center_x':.5,'center_y':.5})
        
        return label
    """
    """def build(self):
        img = Image(
            source='foulgas.png',
            size_hint=(1,.5),
            pos_hint={'center_x':.5,'center_y':.5})
        
        return img"""
    def build(self):
        client.loop_start()
        client.subscribe("CYLINDER WEIGHT")
        client.subscribe("CYLINDER STATUS")
        client.on_message = on_message
        msg = str(client.on_message)
        label = Label(
            text=msg,
            size_hint=(.5,.5),
            pos_hint={'center_x':.5,'center_y':.5}
        )
        time.sleep(50)
        client.loop_end()
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()