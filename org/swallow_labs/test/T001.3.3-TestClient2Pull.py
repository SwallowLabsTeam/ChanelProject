" script to instance a client stub and pull messages from brokers"
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

# getting information from setting file (brokers address and port & client Id)
p = Parser('client2', 'json example')
a = p.get_client_id()
l = p.get_broker_list()
print("ID client: ", a)
for v in l:
    print("Connexion address:", v.address)
    print("Port address :", v.port)

# Client instance (param : client_Id and list of brokers address
c1 = Client(a, l)

# generate client Sockets of cnx with brokers
c1.generate()

# Print sockets cnx port
for h in c1.sock_list:
    print(h.port)

# pull messages
c1.pull()

# print messages (id & priority)
print("Message List :")
for x in c1.pull_list:
    print("capsule id: ", int(x.get_id_capsule()))
    print("capsule priority:", x.get_priority())
    print("*************************************")

