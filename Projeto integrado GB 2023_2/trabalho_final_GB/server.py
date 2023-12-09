# Aplicação do server.
# Recebe as mensagens MQTT e faz o incremento ou decremento da contagem do estoque
# Gera relatório com a quantidade de itens no estoque

# Aplicativo que Recebe a mensagem MQTT quando alguma mercadoria ENTRA ou SAI do estoque

import paho.mqtt.client as mqtt
import time
import random 

#controle de velocidade
velocidade=1
#controle de estoque
stockTotal=5000
tmp_float = 10.0
def stock_control(client, userdata, message, MESSAGE):  
    global stockTotal
    global velocidade
    global tmp_float
    # DO PYTHON 3.10 PRA CIMA, É POSSÍVEL USAR O MATCH/CASE PARA REALIZAR ESTA LÓGICA DE UMA FORMA MAIS LIMPA
    if message.topic == "stock/in":

        if tmp_float < 65:        
            if MESSAGE == "1":
                stockTotal += 500
            elif MESSAGE == "2":
                stockTotal += 1000
            elif MESSAGE == "3":
                stockTotal += 5000
            else:
                print("ERROR IN RAW MATERIAL ENTRY!")
        else:    
            print("Blocked entry of raw material due to high production temperature!")     
    elif message.topic == "stock/tmp":
        tmp = MESSAGE
        print(tmp)
        tmp_float = float(tmp)+(velocidade*3.5)+(stockTotal*0.001)

        print("Current temperature in production: "+str(tmp_float)+ " C")
        
        if tmp_float < 30:
            velocidade = 3
        elif tmp_float < 50 and tmp_float >= 30:
            velocidade = 2
        elif tmp_float <= 80 and tmp_float >= 50:
            print("ATTENTION HIGH TEMPERATURE! REDUCED PRODUCTION SPEED")
            velocidade = 1
        else:
            print("EMERGENCY ALERT SHUTTING OFF THE SYSTEM!")
            exit()
        
        if velocidade == 1:
            ProcessedStock = random.randrange(0,200,1)            
            stockTotal = stockTotal - ProcessedStock
        elif velocidade == 2:
            ProcessedStock = random.randrange(200,400,1)            
            stockTotal = stockTotal - ProcessedStock
        elif velocidade == 3:
            ProcessedStock = random.randrange(400,600,1)            
            stockTotal = stockTotal - ProcessedStock
        else:
            print("ERROR IN PRODUCTION READING!") 

        print(str(ProcessedStock)+" grams produced since last reading")

        
    print("Production operating at speed: "+str(velocidade))
    
    if stockTotal>=0:
        print("Current total raw material in stock is "+ str(stockTotal)+" g")  
    else:
        print("Stock value cannot be less than zero.\nAn error occurred in the inventory count, check the actual quantity and update the system")  

# callback que trata a menssagem recebida
def on_message(client, userdata, message):
    MESSAGE = str(message.payload.decode("utf-8"))
    tempRange= ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    
    if (MESSAGE not in tempRange):
        print("\nReceived message:", MESSAGE)
        print("Topic: " + str(message.topic))
    if (MESSAGE in tempRange):
        
        stock_control(client, userdata, message, MESSAGE)

# instancia o paho client
mqttBroker = "mqtt.eclipseprojects.io"
topic = "stock/#"

msg = "Default message."

client = mqtt.Client("server")  # aqui pode inserir o clientName
# callback das mensagens
client.on_message = on_message
# conecta o client ao broker
client.connect(mqttBroker)

# Subescre o tópico
client.subscribe(topic)

try:
    print("Press CTRL+C to exit")
    client.loop_forever()
except:
    print("Disconnecting do broker.")

client.disconnect()


