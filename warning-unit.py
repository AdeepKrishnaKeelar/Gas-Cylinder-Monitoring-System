"""
The Warning module of the Server 
"""
from easygui import *
from playsound import playsound
message = "WARNING"
title = "WARNING"
ok_button = "CONTINUE"
#playsound('C:\Users\eippe\OneDrive\Desktop\Minor Project\Warning-sound.mp3')
output=msgbox(message)
print(output)