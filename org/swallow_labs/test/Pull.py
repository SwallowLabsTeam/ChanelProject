from org.swallow_labs.model.Client import Client
from org.swallow_labs.test.Adr import Adr


a1=Adr("localhost","6661")
a2=Adr("localhost","6663")
a3=Adr("localhost","6665")
c1=Client("20",[a1,a2,a3])
c1.generate()
print(c1.sock_list[0].port)
print(c1.sock_list[1].port)
print(c1.sock_list[2].port)
c1.pull()
print(c1.pull_list)
for x in c1.pull_list:

    print(x.get_priority())
