from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority

id_client = 10
capsule = Capsule(id_client)
capsule.set_type("PAYLOAD")
capsule.set_payload({'nom': 'gammoudi', 'prenom': 'seif'})
capsule.set_id_receiver("20")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
