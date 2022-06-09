"""
This is the Python Kivy Application to house the data from the broker
A trial application is built using the open source Kivy Library
Install Kivy by using pip3/pip install kivy
"""
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(
            text='FOULGAS APPLICATION',
            size_hint=(.5,.5),
            pos_hint={'center_x':.5,'center_y':.5})
        
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()