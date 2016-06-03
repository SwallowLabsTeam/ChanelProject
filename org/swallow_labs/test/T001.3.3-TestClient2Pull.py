" script to instance a client stub and pull messages from brokers"
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

# getting information from setting file (brokers address and port & client Id)
p = Parser('client2', 'json example')
a = p.get_client_id()
l = p.get_broker_list()

# Client instance (param : client_Id and list of brokers address
c1 = Client(a, l)

# generate client Sockets of cnx with brokers
c1.generate()

# Print sockets cnx port


# pull messages
if c1.pull():
    for x in c1.pull_list:
        print("Capsule received")