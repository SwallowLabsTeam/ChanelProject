import json
import socket
from multiprocessing import Process
from org.swallow_labs.model.Broker import Broker
import time


class Launcher:
    """
        Class creating a BrokerData object
        G{classtree}
        DESCRIPTION
        ===========
        Class that launches the brokers according to the configuration file

        @param path:    the path of the configuration file

        @type path: string

    """
    def __init__(self, path):
        self.p = {}
        json_data = open(path).read()
        data = json.loads(json_data)
        for i in range(len(dict(data)['ip_add'])):
            if socket.gethostbyname(socket.gethostname()) == dict(data)['ip_add'][i]:
                self.p[i] = Process(target=self.broker_def, args=(dict(data)['front_end'][i], dict(data)['back_end'][i]))
                self.p[i].start()
                time.sleep(0.01)

    @staticmethod
    def broker_def(front_end, back_end):
        b = Broker(front_end, back_end)
        print("broker launched")
        print(str(front_end) + "///" + str(back_end))
        b.start()
