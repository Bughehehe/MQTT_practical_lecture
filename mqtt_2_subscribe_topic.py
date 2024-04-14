import paho.mqtt.client as mqtt

broker_address = "localhost"
broker_port = 1883
topic = "python"

# Callback function for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe(topic)

# Callback function for when a message is received from the server
def on_message(client, userdata, msg):
    print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "'")
    variable = str(msg.payload)
    print("Variable:", variable)
    # Unsubscribe from the topic after receiving the message
    client.unsubscribe(topic)
    # Disconnect from the broker
    client.disconnect()

# Create a MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Start the network loop
client.loop_forever()
