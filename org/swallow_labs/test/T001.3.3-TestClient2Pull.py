" script to instance a client stub and pull messages from brokers"
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

p = Parser('../configuration/Configuration.json', 'client2')
a = p.get_client_id()
l = p.get_broker_list()
c1 = Client(a, l)
print("Client launched")
c1.generate()
if c1.pull():
    if len(c1.pull_list) == 0:
        print("No Messaages")
    else:
        for x in c1.pull_list:
            print("Capsule received")