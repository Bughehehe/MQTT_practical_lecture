import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
broker_port = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

client.connect(broker_address, broker_port, 60)


message = "1"
client.publish("node_red_flip/state", message)



