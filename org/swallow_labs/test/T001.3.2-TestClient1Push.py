'''Script to instance a client stub and push two capsule'''
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.model.Parser import *
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
p = Parser('client', 'json example')
a = p.get_client_id()
l = p.get_broker_list()
print("ID client: ", a)
for v in l:
    print("Connexion address:", v.address)
    print("Port address :", v.port)
c = Client(a, l)
capsule = Capsule(c.id_client)
capsule.set_type("PAYLOAD")
capsule.set_payload({'nom': 'gammoudi', 'prenom': 'seif'})
capsule.set_id_receiver("20")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule2 = Capsule(c.id_client)
capsule2.set_type("PAYLOAD")
capsule2.set_payload({'nom': 'Sallemi', 'prenom': 'Akram'})
capsule2.set_id_receiver("20")
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
c.generate()
c.push(capsule2)
c.push(capsule)

