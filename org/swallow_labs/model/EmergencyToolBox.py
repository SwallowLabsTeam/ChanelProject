from org.swallow_labs.model.Broker import*
import socket
from org.swallow_labs.model.Capsule import *
from org.swallow_labs.tool.CapsulePriority import *
import hashlib


class EmergencyToolBox:

    def __init__(self, path):
        self.path = path
        parse_obj = Parser(self.path)
        self.file_store = parse_obj.get_param_snapshot()

    def store(self,element_list, obj):
        a = {'date': time.ctime(),
             'broker_info': {"adr": socket.gethostbyname(socket.gethostname()), "backend": str(obj.id_backend),
                             "frontend": str(obj.id_frontend)}}

        a['msg_list']=[]
        for x in element_list:
             a['msg_list'].append(x.__dict__)
        with open(self.file_store, "w") as json_file:
            json.dump(a, json_file)
            self.hash_org = hashlib.md5(str(a).encode("utf-8")).hexdigest()
            # print(hashlib.md5(str(a).encode("utf-8")).hexdigest())

    def snapshot(self, obj):
        element_list = obj.snapshot()
        self.store(element_list, obj)

    def reload(self):

        son_data = open(self.file_store).read()
        data = json.loads(son_data)
        li=[]
        for x in data["msg_list"]:
            c=Capsule()
            c.set_id_receiver(x["id_receiver"])
            c.id_capsule=x["id_capsule"]
            c.set_payload(x["payload"])
            c.id_sender=x["id_sender"]
            c.set_priority(x["priority"])
            c.set_sending_date(x['sending_date'])
            c.set_status_capsule(x['status_capsule'])
            c.set_type(x['type'])
            li.append(c)

        b = Broker(data['broker_info']['frontend'], data['broker_info']['backend'])
        b.message_list = li
        return (b)








b=Broker(4444,4442)
capsule = Capsule("4")
capsule.set_type("PAYLOAD")
capsule.set_payload({'nom': 'gammoudi', 'prenom': 'seif'})
capsule.set_id_receiver("20")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule2 = Capsule("6")
capsule2.set_type("PAYLOAD")
capsule2.set_payload({'nom': 'Sallemi', 'prenom': 'Akram'})
capsule2.set_id_receiver("20")
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
b.message_list=[capsule,capsule2]

p=EmergencyToolBox("../conf/Configuration.json")
p.store(b.message_list,b)
p.snapshot(b)
k=p.reload()

print(k.id_backend)
print(k.id_frontend)
for x in k.message_list:
    print(x.print_capsule())
print(p.hash_org)
#print(k)
#print(k['broker_info']['backend'])
#l=k["msg_list"]
#print(l)
#for x in k["msg_list"]:
    #print(x.get_payload()["prenom"])