#For the MQTT Client, install by the command sudo pip3 install paho.mqtt
#To check the push messages, install Gotify-Server and the receiver app, include the IP address.
import paho.mqtt.client as mqtt
import time
import serial
import requests
import re
import threading
import sys
import os

GasLeak_Flag = 0
LowGas_Flag = 0
EmergencyGas_Flag = 0

#SMS Sending function
def send_SMS():
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {
        "authorization": "", #Make your account in Fast2SMS
        "message": "There's a gas leakage, please check it immediately",
        "language": "english",
        "route": "q",
        "numbers": "9606740404" }
    headers = {
        'cache-control': "no-cache"
    }
    try:
        if GasLeak_Flag > 0:
            response = requests.request("GET",url,headers= headers, params = querystring)
            print("SMS Sent")

    except:
        print("Failed!")


#Function to send the push message
def send_message():
    url = "http://192.168.72.253/message?token=AeZv7ML-pvR5nni"
    data = {
        "title":"GAS LEAK",
        "message":"THERE HAS BEEN A GAS LEAK, CHECK IMMEDIATELY!"
    }
    requests.post(url,data)


#Function to check for the gas leakage
def readGasValue(GasReading):
    GasRealValue = int(re.search(r'\d+',GasReading).group(0))
    print(GasRealValue)
    if GasRealValue >= 70:
        print("Leakage detected")
        GasLeak_Flag=1
        send_message()
        send_SMS()
        os._exit(os.EX_OK)

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

while True or GasLeak_Flag!=0:
    if(ser.in_waiting>0):
        #Reading the values
        Gas_value=ser.readline().decode('utf-8').rstrip()
        Gas_value = Gas_value+" is the new gas reading"
        print(Gas_value)
        #threaded calls for threads parallely running to process a gas-leak
        t1 = threading.Thread(target=readGasValue,args=(Gas_value,))
        t1.start()
        t1.join()
        ser.flushInput() #Flushing Serial Monitor
        weight=ser.readline().decode('utf-8').rstrip()
        print("Weight Value - "+weight)
        client.publish("CYLINDER WEIGHT",weight)
        print("Value has been published!") #MQTT-Protocol publishing success message
