" script to instance a client stub and pull messages from brokers"
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

p=Parser('client', 'json example')
a=p.get_client_id()
l=p.get_broker_list()
print("ID client: ",a)
for v in l:
    print("Connexion address:", v.address)
    print("Port address :", v.port)
c1=Client(a,l)
c1.generate()

for h in c1.sock_list:
    print(h.port)
c1.pull()
print("Message List :")
for x in c1.pull_list:


    print("capsule id: ", int(x.get_id_capsule()))
    print("capsule priority:", x.get_priority())
    print("*************************************")

