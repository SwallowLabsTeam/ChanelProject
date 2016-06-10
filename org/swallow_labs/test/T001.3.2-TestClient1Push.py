'''Script to instance a client stub and push two capsule'''
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.model.Parser import *
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
p = Parser( '../configuration/Configuration.json', 'client')
a = p.get_client_id()
l = p.get_broker_list()
c = Client(a, l)
print("client launched")
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
if c.push(capsule2) == 1:
    print("Capsule Sent")
if c.push(capsule) == 1:
    print("Capsule Sent")

