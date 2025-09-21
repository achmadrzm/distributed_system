import paho.mqtt.client as mqtt
import sys
import datetime

broker = "mqtt-broker-mod"
port = 1883
topics = ["sister/temp", "sister/humidity"]

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Connected to {broker}")
        for topic in topics:
            client.subscribe(topic)
            print(f"Subscribed to {topic}")
    else:
        print(f"Connection failed, code {rc}")
        sys.exit(1)

def on_message(client, userdata, message, properties=None):
    print(f"[{datetime.datetime.now()}] {message.topic} -> {message.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(broker, port, keepalive=60)
except Exception as e:
    print(f"Failed to connect: {e}")
    sys.exit(1)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Subscriber stopped")
    client.disconnect()