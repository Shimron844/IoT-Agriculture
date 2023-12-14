import serial
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM4'
ser.open()
print(ser.is_open)
while 1:
       line = ser.readline()
       output = line.decode()
       print(output)
    

