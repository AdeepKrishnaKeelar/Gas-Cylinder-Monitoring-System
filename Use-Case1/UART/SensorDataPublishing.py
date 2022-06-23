#For the MQTT Client, install by the command sudo pip3 install paho.mqtt
import paho.mqtt.client as mqtt
import time
import serial

client = mqtt.Client("Cylinder Data") #MQTT BROKER
client.connect("broker.hivemq.com") # HOST
# http://www.hivemq.com/demos/websocket-client/ 
# Check the readings here 
print("Connection Established!")

#Establishing USB UART Protocol between Arduino and RPi
#The slave Arduino sends the readings to the RaspberryPi
#A serial communication is established by Universal Serial Bus Cable
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.flush()

while(1):
    if(ser.in_waiting>0):
        #Reading the values
        line=ser.readline().decode('utf-8').rstrip()
        print(line+" is the reading")
        client.publish("CYLINDER WEIGHT",line) #Publishing the data
        print("Just published above reading")


