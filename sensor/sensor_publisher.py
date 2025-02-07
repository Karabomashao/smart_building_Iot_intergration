import paho.mqtt.client as mqtt
import time
import random


BROKER = "localhost"
PORT = 1883
KEEP_ALIVE = 60
TOPIC = "sensors/temperature/{}"
SENSORS = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5"] #Five sensors for 5 rooms in the building

client = mqtt.Client()  #Creating client object
client.connect(BROKER, PORT, KEEP_ALIVE) #Connecting to the broker and checking connection every 60 seconds

try:
    while True:
        for sensors in SENSORS:
            temperature = round(random.uniform(15, 35), 2)
            topic = TOPIC.format(sensors)
            message = f"{temperature}\u00b0C"

            client.publish(topic, message, qos=1)
            print(f"Published: {message} to {topic}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopping sensor simulation")
    client.disconnect()

    


