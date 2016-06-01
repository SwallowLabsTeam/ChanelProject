import json
import socket
from multiprocessing import Process
from org.swallow_labs.model.Broker import Broker


def broker_def(front_end, back_end):
    b = Broker(front_end, back_end)
    print("broker launched")
    print(str(front_end)+"///"+str(back_end))
    b.start()




def broker_launcher(path):
    p = {}
    json_data = open(path).read()
    data = json.loads(json_data)
    for i in range(len(dict(data)['ip_add'])):
        if socket.gethostbyname(socket.gethostname()) == dict(data)['ip_add'][i]:
            p[i] = Process(target=broker_def, args=(dict(data)['front_end'][i], dict(data)['back_end'][i]))
            p[i].start()
    return p
if __name__ == '__main__':
    p = broker_launcher('json example')