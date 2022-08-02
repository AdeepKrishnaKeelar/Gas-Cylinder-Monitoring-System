#For the MQTT Client, install by the command sudo pip3 install paho.mqtt
import paho.mqtt.client as mqtt
import time
import serial
import requests
import re

GasLeak_Flag = 0
LowGas_Flag = 0
EmergencyGas_Flag = 0

def send_SMS():
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {
        "authorization": "ImXyat19xoJfRqc0DABzeKVC4iuGQhEO5ZrdpvFL6YkNHwPTl8KtGIMrRvHofiPgzmB2xWVJXdShpUFu",
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

def GasLeak_Emergency():
    if GasLeak_Flag > 0:
        send_SMS()

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
        Gas_value=ser.readline().decode('utf-8').rstrip()
        Gas_value = Gas_value+" is the new gas reading"
        print(Gas_value)
        GasRealValue = int(re.search(r'\d+',Gas_value).group(0))
        if GasRealValue > 70:
            print("Leakage detected!")
            GasLeak_Flag = 1
            GasLeak_Emergency()
            break
        ser.flushInput()
        weight=ser.readline().decode('utf-8').rstrip()
        print("Weight Value - "+weight)
        client.publish("CYLINDER WEIGHT",weight)
        print("Value has been published!")


