import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "xlgdck"
deviceType = "Gas_final"
deviceId = "gas"
authMethod = "token"
authToken = "Yovnne@123"

# Initialize GIPO

Temperature=random.randint(0,100)
Humidity=random.randint(0,100)
Pulse=random.randint(0,100)
Oxygen=random.randint(0,100)
Latitude = random.randint(0,100)
Longtitude = random.randint(0,100)

def myCommandCallback(cmd):
    print("Command received: %s" %cmd.data['command'])
    status=cmd.data['command']
    if status=="lighton":
        print("LED is ON")
    else :
        print("LED is OFF")
    print (cmd)


try:
        deviceOptions = {"org":organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,"auth-token": authToken}
                       
        deviceCli = ibmiotf.device.Client(deviceOptions)
        #...............................................

except Exception as e:
        print("Caught exception connecting device: %s" % str(e))
        sys.exit()

#Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
    #Get Sensor Data from DHT11
    Temperature=random.randint(0,100)
    Humidity=random.randint(0,100)
    Pulse=random.randint(0,100)
    Oxygen=random.randint(0,100)
    Latitude = random.randint(0,100)
    Longtitude = random.randint(0,100)

    
    data = {"d":{'Temperature': Temperature, 'Humidity' : Humidity, 'Pulse':Pulse,'Oxygen':Oxygen,"Latitude":Latitude,"Longtitude":Longtitude}}
    #print data
    def myOnPublishCallback():
        print("Published Temperature = %s c" % Temperature,"Humidity = %s %%" % Humidity, "Pulse = %s BPM" % Pulse, "Oxygen = % s mgL " % Oxygen , "Latitude = % s Degrees" % Latitude
              , "Longtitude = %s Degrees" % Longtitude,"to IBM Watson")

    success = deviceCli.publishEvent("IoTSensor","json",data,qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(1)

    deviceCli.commandCallback = myCommandCallback

#Disconnect the device and application from the cloud
deviceCli.disconnect()
