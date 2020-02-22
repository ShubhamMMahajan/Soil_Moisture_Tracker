import serial
import time
ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0,1]
while True:
    read_serial=ser.readline()
    serial_decoded = read_serial.decode("utf-8").strip()
    print(serial_decoded)
    time.sleep(1)
