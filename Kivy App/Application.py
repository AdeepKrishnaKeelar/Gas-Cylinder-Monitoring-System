"""
This is the Python Kivy Application to house the data from the broker
A trial application is built using the open source Kivy Library
Install Kivy by using pip3/pip install kivy
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MainApp(App):
    """def build(self):
        label = Label(
            text='FOULGAS APPLICATION BY APEED',
            size_hint=(.5,.5),
            pos_hint={'center_x':.5,'center_y':.5})
        
        return label
    """
    def build(self):
        img = Image(
            source='foulgas.png',
            size_hint=(1,.5),
            pos_hint={'center_x':.5,'center_y':.5})
        
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()