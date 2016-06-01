from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.test.Adr import Adr
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
import time

a1 = Adr("localhost", "6662")
a2 = Adr("localhost", "6664")
a3 = Adr("localhost", "6666")
c = Client("2", [a1, a2, a3])

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
