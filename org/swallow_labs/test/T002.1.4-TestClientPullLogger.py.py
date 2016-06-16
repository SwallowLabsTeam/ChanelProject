"Script to instance a client object and pull messages from all brokers and log all msg"

from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *


parser = Parser('../conf/Configuration.json', 'client2')
client_id = parser.get_client_id()
broker_list = parser.get_broker_list()
client = Client(client_id, broker_list)
print("Client launched")

client.generate()
if client.pull():
    if len(client.pull_list) == 0:
        print("No Messages")
    else:
        for x in client.pull_list:
            print("Capsule received")
