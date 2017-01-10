'''Script to instance a client stub and push two capsule'''
from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleSort import CapsuleSort
from org.swallow_labs.tool.CapsuleType import CapsuleType
import org.swallow_labs.model.RunClient

l = Parser.get_backend_broker_list()
c = Client(45, l)
print("client launched")
capsule = Capsule(c.id_client, CapsuleType.PAYLOAD)
# capsule.set_type("PAYLOAD")
capsule.set_payload({'nom': 'gammoudi', 'prenom': 'seif'})
capsule.set_id_receiver("20")
capsule.set_sort(CapsuleSort.BOOKING_MSG)
#capsule.set_id_receiver("25")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule2 = Capsule(c.id_client, CapsuleType.PAYLOAD)
# capsule2.set_type("PAYLOAD")
capsule2.set_payload({'nom': 'Sallemi', 'prenom': 'Akram'})
capsule2.set_id_receiver("20")
capsule2.set_sort(CapsuleSort.BOOKING_MSG)
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
c.generate()
if c.push(capsule2) == 1:
    print("Capsule Sent")
    print(capsule2.print_capsule())
if c.push(capsule) == 1:
    print("Capsule Sent")
    print(capsule.print_capsule())

