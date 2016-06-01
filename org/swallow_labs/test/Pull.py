from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

p=Parser('client', 'json example')
a=p.get_client_id()
l=p.get_broker_list()
print(a)
for v in l:
    print(v.address)
    print(v.port)
c1=Client(a,l)
c1.generate()

for h in c1.sock_list:
    print(h.port)
c1.pull()
print(c1.pull_list)
for x in c1.pull_list:

    # print(x.get_priority())
    print(int(x.get_id_capsule()))
