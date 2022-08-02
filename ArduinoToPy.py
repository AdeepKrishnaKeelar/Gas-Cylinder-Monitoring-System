import serial

ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.flush()

while(1):
    if(ser.in_waiting>0):
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
