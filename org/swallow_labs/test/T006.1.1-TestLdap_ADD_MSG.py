from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsulePriority import CapsulePriority
from org.swallow_labs.tool.CapsuleType import CapsuleType
from org.swallow_labs.tool.CapsuleSort import *

import time
from org.swallow_labs.model.SendProcessor import *
import org.swallow_labs.model.SendProcessor
l = Parser.get_backend_broker_list()
c = Client(77, l)
c.generate()
print("client launched")
capsule = Capsule(c.id_client, CapsuleType.PAYLOAD)
# capsule.set_type("PAYLOAD")

capsule.set_payload({'att':['dn','objectClass','Eadress','Ebalance','ECode','EEmail','Efax','Ename','Ephone','ESector','EShortName','EuserAccountNum'],
                     'dn': 'ECode=101,o=Establishments,o=WebApp,dc=swallow,dc=tn',
                     'objectClass': ['top','ClientEstablishment'],
                     'Eadress': 'route el sokra',
                     'Ebalance': '444',
                     'ECode': '101',
                     'EEmail': 'ooredoo@ooredoo.com',
                     'Efax': '74555755',
                     'Ename': 'ooredoo',
                     'Ephone': '74545454',
                     'ESector': 'telecominucation',
                     'EShortName': 'ord',
                     'EuserAccountNum': '74'
                     })


capsule.set_id_receiver("55")
#capsule.set_id_recNOeiver("25")
capsule.set_priority(CapsulePriority.BOOKING_MSG)
capsule.set_sort(CapsuleSort.LDAP_ADD_MSG)

capsule2 = Capsule(c.id_client, CapsuleType.PAYLOAD)
# capsule2.set_type("PAYLOAD")
capsule2.set_payload({'nom': 'Sallemi', 'prenom': 'Akram'})
capsule2.set_id_receiver("55")
capsule2.set_priority(CapsulePriority.INFORMATION_DEVICE_MSG)
capsule2.set_sort(CapsuleSort.LDAP_ADD_MSG)
s=SendProcessor(capsule)
s.send_capsule(c)
print("send")
for x in org.swallow_labs.model.SendProcessor.sending_list:
    print(x.print_capsule())

time.sleep(5)
'''if c.push(capsule) == 1:
    print("capsule resended")
    print(capsule.id_sender)'''
'''time.sleep(5)
if c.push(capsule) == 1:
    print("capsule resended")
    print(capsule.id_sender)

time.sleep(5)
if c.push(capsule2) == 1:
    print("capsule2 sended")
    print(capsule2.id_sender)
time.sleep(5)
if c.push(capsule2) == 1:
    print("capsule resended")
    print(capsule2.id_sender)

time.sleep(5)
if c.push(capsule2) == 1:
    print("capsule resended")
    print(capsule2.id_sender)'''
#time.sleep(5)
print(c.id_client)
if c.pull():
    if len(c.pull_list) == 0:
        print("No Messaages")
    else:
        for x in c.pull_list:
         print(x.print_capsule())
         print("ACKAAAAAA:", type(x.get_ACK()))

         if (x.get_ACK() == str("YES")):
            pld = x.get_payload()
            print("capsule ack")
            print(pld["id"])
            print("ACKAAAAAA:", x.get_ACK())
            for w in org.swallow_labs.model.SendProcessor.sending_list:
                print("plddddd ",w.get_id_sender())
                if (w.get_id_capsule() == pld["id"]):
                    print("ok")
                    org.swallow_labs.model.SendProcessor.sending_list.remove(w)

for x in org.swallow_labs.model.SendProcessor.sending_list:
    print(x)
