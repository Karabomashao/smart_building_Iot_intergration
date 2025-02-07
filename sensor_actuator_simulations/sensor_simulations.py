import paho.mqtt.client as mqtt
import time
import random


BROKER = "localhost"
PORT = 1883
TOPIC_TEMPLATE = "sensors/temperature/{}"
SENSORS = ["sensor1", "sensor2", "sensor3", "sensor4", "sensor5"]

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

try:
    while True:
        for sensors in SENSORS:
            temperature = round(random.uniform(15, 35), 2)
            topic = TOPIC_TEMPLATE.format(sensors)
            message = f"{temperature}\u00b0C"

            client.publish(topic, message, qos=1)
            print(f"Published: {message} to {topic}")

        time.sleep(2)

except KeyboardInterrupt:
    print("Stopping sensor simulation")
    client.disconnect()

    


