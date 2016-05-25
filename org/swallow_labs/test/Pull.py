from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule

c = Client("20", "localhost:5560")
k = c.pull()
for i in k:
    print(i.get_payload()["nom"])
    print(i.get_date())
