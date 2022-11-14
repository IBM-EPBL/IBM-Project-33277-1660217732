#IBM Watson IOT Platform
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "834zz1",
        "typeId": "weather_device",
        "deviceId":"weather1234"
    },
    "auth": {
        "token": "PramodGabrieal123456"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    hazg=random.randint(0,100)
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    press=random.randint(0,80)
    myData={'HazardousGasLevel':hazg,'temperature':temp, 'humidity':hum, 'pressure':press,}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
