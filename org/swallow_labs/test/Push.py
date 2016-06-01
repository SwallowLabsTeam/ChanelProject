from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.model.Parser import *
from org.swallow_labs.tool.CapsulePriority import CapsulePriority

p=Parser('client2', 'json example')
a=p.get_client_id()
l=p.get_broker_list()
print(a)
for v in l:
    print(v.address)
    print(v.port)

c = Client(a,l)

capsule = Capsule(c.id_client)
capsule.set_type("PAYLOAD")
capsule.set_payload({'nom': 'seif', 'prenom': 'gamoudi'})
capsule.set_id_receiver("20")

capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule2 = Capsule(c.id_client)
capsule2.set_type("PAYLOAD")
capsule2.set_payload({'nom': 'aaaa', 'prenom': 'bbbb'})
capsule2.set_id_receiver("20")
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
# time.sleep(1)
capsule3 = Capsule(c.id_client)
capsule3.set_type("PAYLOAD")
capsule3.set_payload({'nom': 'zzzzz', 'prenom': 'bbbb'})
capsule3.set_id_receiver("20")
capsule3.set_priority(CapsulePriority.UPDATE_MSG)
c.generate()
c.push(capsule)
c.push(capsule)
c.push(capsule2)
c.push(capsule)
c.push(capsule3)
c.push(capsule)
c.push(capsule2)
