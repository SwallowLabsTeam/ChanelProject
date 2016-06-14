from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority

p = Parser('../configuration/Configuration.json', 'client')
id_client = p.get_client_id()
connexions = p.get_broker_list()
client = Client(id_client, connexions)
print("Client launched")

capsule = Capsule(client.id_client)
capsule.set_type("PAYLOAD")
capsule.set_payload({'nom': 'XXXX', 'prenom': 'YYYY'})
capsule.set_id_receiver("20")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
client.generate()
if client.push(capsule) == 1:
    print("Capsule Sent")
