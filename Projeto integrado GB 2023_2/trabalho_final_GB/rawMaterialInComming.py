# Aplicativo que publica a mensagem MQTT quando alguma mercadoria ENTRA no estoque

import paho.mqtt.client as mqtt
import sys
import socket
import time
import keyboard

# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("rawMaterialInComming")  # aqui pode inserir o clientName
topic = "stock/in"
msg = "Raw material entry detected!"

# cria a conexão com o broker e verifica se a conexão deu certo
if client.connect(mqttBroker) != 0:
    print("No connection to the broker!")
    sys.exit(-1)

while True:
    # ARGUMENTOS(tópico, mensagem de payload, nível de qualidade do serviço)
    if keyboard.read_key() == "1":
        client.publish(topic, msg, 0)
        print("Message published -> Topic: " + topic + " Message: " + msg)
        client.publish(topic, "1", 0)
        print("Raw material added to the production flow-> 500g.")
        time.sleep(1)
    if keyboard.read_key() == "2":
        client.publish(topic, msg, 0)
        print("Message published -> Topic: " + topic + " Message: " + msg)
        client.publish(topic, "2", 0)
        print("Raw material added to the production flow-> 1kg.")
        time.sleep(1)
    if keyboard.read_key() == "3":
        client.publish(topic, msg, 0)
        print("Message published -> Topic: " + topic + " Message: " + msg)
        client.publish(topic, "3", 0)
        print("Raw material added to the production flow-> 5kg.")
        time.sleep(1)

# desconecta do broekr
# client.disconnect()
