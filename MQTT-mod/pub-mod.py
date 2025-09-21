import paho.mqtt.client as mqtt
import time
import random
import sys

broker = "mqtt-broker-mod"
port = 1883

topics = ["sister/temp", "sister/humidity"]

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Connected to {broker}")
    else:
        print(f"Connection failed, code {rc}")
        sys.exit(1)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

try:
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"Failed to connect: {e}")
    sys.exit(1)

try:
    while True:
        suhu = random.randint(20, 35)
        humidity = random.randint(40, 70)
        client.publish("sister/temp", f"Suhu: {suhu}°C")
        client.publish("sister/humidity", f"Humidity: {humidity}%")
        print(f"Published: Suhu={suhu}°C, Humidity={humidity}%")
        time.sleep(1)
except KeyboardInterrupt:
    print("Publisher stopped")
    client.disconnect()