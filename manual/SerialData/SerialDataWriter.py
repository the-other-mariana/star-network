import serial
import re
from datetime import datetime
import csv
import os.path

def formattedData(d, now):
    global p


    try:
        # Get the relevant data to save it into a File
        a = re.search(r'Addr=\D*(0x\d+)', d).group(1)
        t = re.search(r'Temp=\D*(\d+)', d).group(1)
        r = re.search(r'RSSI=\D*(-\d+)', d).group(1)
        n = re.search(r'Number of Joined Devices: \D*(\d+)', d).group(1)

        print(a, t, r, now.date(), now.time(), n, "\n")

        row = [a, t, r, now.date(), now.time(), n]

        if os.path.isfile(p + '_' + a + '.csv'):
            with open(p + '_' + a + '.csv', 'a+', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(row)
        else:
            with open(p + '_' + a + '.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(['Address', 'Temperature', 'RSSI', 'Date', 'Time', 'Num of devices'])
                writer.writerow(row)

    except:
        print("None")

#Ask for the port where the Collector is connected in format: 'COM' + #. i.e. COM4
p = input("Serial port: ")

serialPort = serial.Serial(port = p, baudrate=115200, bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)

serialString = ""                           # Used to hold data coming over UART


while(1):

    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):
        # Get the exact time at which the port stopped waiting
        now = datetime.now()
        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        data = serialString.decode('UTF-8')

        formattedData(data, now)

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        #serialPort.write(b"Thank you for sending data \r\n")
