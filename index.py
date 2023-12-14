from flask import *
import datetime
import time
import logging as logger
import serial
import random
from flask_session import *


logger.basicConfig(level="DEBUG")


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


app = Flask(__name__,static_folder='static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def home():
    return render_template('setup.html')


@app.route('/status', methods=['GET'])
def status():
     data = 'Server Status Ok'
     return Response(data, mimetype='application/json')
     

@app.route('/connect', methods=['POST'])
def connect():
    req = request.get_json()
    port = req['port']
    baudrate = req['baudrate']
    session["port"] = req['port']
    session["baudrate"] = req['baudrate']
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    try:
       ser.open()
       if ser.is_open:
        line = ser.readline()
        output = line.decode()
        print(output)
        ser.close()
        return 'CONNECTED'                 
    except:
       print("An exception occurred")
    return 'DISCONNECTED'


@app.route('/get-data', methods=['POST'])
def get_data():
    port = session["port"]
    baudrate = session['baudrate']
    temperature = str(random.randrange(1,100))
    humidity = str(random.randrange(1,100))
    moisture = str(random.randrange(1,100))
    print(type(temperature))
    muck = temperature + "," + humidity + "," + moisture
    print(color.BOLD + "Arduino Serial Master\t " + port  + color.END + "\n")
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    ser.open()
    if ser.is_open:
        line = ser.read(15)
        output = line.decode()
        print('-----')
        print(output)
        # ser.close()
        return output
    else:
     return "muck"



@app.route('/start-motor', methods=['POST'])
def start_motor():
    port = session["port"]
    baudrate = session['baudrate']
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    ser.open()
    if ser.is_open:
        ser.write(b'H')
        # ser.close()
        return "LED HIGH"
    else:
     return "LED OFF"


@app.route('/stop-motor', methods=['POST'])
def stop_motor():
    port = session["port"]
    baudrate = session['baudrate']
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    ser.open()
    if ser.is_open:
        ser.write(b'L')
        ser.close()
        return "LED HIGH"
    else:
     return "LED OFF"




@app.route('/application')
def application():
   return render_template('index.html')



@app.route('/map')
def map():
   return render_template('map.html')


@app.route('/chart')
def chart():
   return render_template('chart.html')


@app.route('/setup')
def setup():
   return render_template('setup.html')




# main driver function
if __name__ == '__main__':

    logger.debug("Server Starting ")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)