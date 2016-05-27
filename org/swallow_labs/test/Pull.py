from org.swallow_labs.model.Client import Client

c = Client("20", "localhost","4432")
k = c.pull()
if k == 0:
    print("closed Server")
else:
    for i in k:
        print(i.get_payload()["nom"])