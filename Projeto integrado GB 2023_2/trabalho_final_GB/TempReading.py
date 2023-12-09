# Aplicativo que envia a mensagem MQTT quando alguma mercadoria SAI do estoque

import paho.mqtt.client as mqtt
import sys
import socket
import time
import keyboard
import random 
 


# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("tempRead")  # aqui pode inserir o clientName
topic = "stock/tmp"
msg = "Temp reading detected!"
machineSpeed = 1
 

# cria a conexão com o broker e verifica se a conexão deu certo
if client.connect(mqttBroker) != 0:
    print("No connection to the broker!")
    sys.exit(-1)

while True:

    #simula leitura da temperatura
    tmp=random.randrange(1,12,1)
    tmp_as_string = str(tmp)
    client.publish(topic, msg, 0)
    print("Message published -> Topic: " + topic + " Message: " + msg)
    client.publish(topic, tmp_as_string, 0)
    print("Temperatura enviada")
    time.sleep(7)



# desconecta do broekr
# client.disconnect()
