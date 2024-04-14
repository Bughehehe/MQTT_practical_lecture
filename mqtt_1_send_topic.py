import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
broker_port = 1883

# Create a MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Publish topic
message = "Hello MQTT!"
client.publish("python", message)