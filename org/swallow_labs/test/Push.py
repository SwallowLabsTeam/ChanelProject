from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule

c = Client("10", "localhost","4431")

capsule = Capsule(c.id_client)
capsule.set_type("PAYLOAD")
capsule.set_payload({'nom': 'seif', 'prenom': 'gamoudi'})
capsule.set_status_capsule("NOTSENT")


capsule.set_id_receiver("20")
c.push(capsule)