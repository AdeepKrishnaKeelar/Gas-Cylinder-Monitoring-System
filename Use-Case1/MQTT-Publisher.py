#A simulation of the minor project's working of the hardware
#Using MQTT protocol, sending the cylinder's calibrated reading to the MQTT
#MQTT is Message Query Telematry Transport Protocol
#The cylinder data is published, the subscriber will receive it's signal.
# Use sudo pip3 install paho-mqtt
#Suppose requests fail, use pip3 install requests
#Check readings @ http://www.hivemq.com/demos/websocket-client/
#The Fast2SMS API link be @ https://www.fast2sms.com/
#Make an account and get the Dev-API Key
import paho.mqtt.client as paho #mqtt library of Python (one of them)
import time
import random
import requests #To ping a website or portal
main_cylinder_weight=15 #An estimated guess of an empty cylinder with no gas 15.9 be right, rounded
loop_flag = True

#function for calibration for weight of cylinder
def calibrate(cylinder_weight):
    rem_weight=cylinder_weight-main_cylinder_weight
    return rem_weight

#function for calibration in a detailed way: 100 - Full, 75 - Three Quarters, 50 - Half,X
#25 - Quarter filled and 0 - Dangerously 5-10% 
def calibrate_signal(cylinder_weight):
    if 20<=cylinder_weight<=25:
        return 'Full'
    elif 15<=cylinder_weight<=20:
        return 'Three Quarters.'
    elif 10<=cylinder_weight<=15:
        return 'Half Full'
    elif 5<=cylinder_weight<=10:
        return 'Quarter Fill'
    elif 0<=cylinder_weight<=5:
        return 'Dangerously Low'
    else:
        return 'Error'

client = paho.Client("Cylinder Data") #Client Broker
client.connect("broker.hivemq.com") #Connecting to MQTT

#while true
while(loop_flag):
    cylinder_weight=random.randint(15,40) #Randomly generating values
    cylinder_weight=calibrate(cylinder_weight)
    cylinder_signal=calibrate_signal(cylinder_weight)
    client.publish("CYLINDER WEIGHT",cylinder_weight) #Publishing the values
    client.publish("CYLINDER STATUS",cylinder_signal) #Publishing the signal
    print("Printed value - "+str(cylinder_weight)+" and signal - "+cylinder_signal) #Reference
    print("----------------------------")
    #if signal calibrated to be dangerously low or quarter fill, then break from the loop
    if cylinder_signal=='Dangerously Low':
        loop_flag=False
        flag=0
    time.sleep(5)

#if loop is broken
#It uses a REST API
"""if flag==0:
    url = "https://www.fast2sms.com/dev/bulkV2"
    querystring = {
        "authorization": "ImXyat19xoJfRqc0DABzeKVC4iuGQhEO5ZrdpvFL6YkNHwPTl8KtGIMrRvHofiPgzmB2xWVJXdShpUFu", #I ain't mentioning it here, hAcKeRs wiLL sTeaL iT
        "message": "Your cylinder is very low on gas, an order has been sent!", #SMS Body message
        "language": "english",
        "route": "q",
        "numbers": "9606740404"} #Insert yo phone numbers here
  
    headers = {
        'cache-control': "no-cache"
    }
    #Exception to see whether the message sending is successful
    try:
        response = requests.request("GET", url, headers = headers, params = querystring)
        print("SMS Successfully Sent")
    
    except:
        print("Oops! Something wrong")"""