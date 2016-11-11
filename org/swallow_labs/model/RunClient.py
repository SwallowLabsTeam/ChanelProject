from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Capsule import Capsule
from multiprocessing import Process
import time
class RunClient:
    """
        Class creating a RunClient object
        G{classtree}
        DESCRIPTION
        ===========
        Class that launches a Client in a routine

        @param id_client    : a client id
        @param list_address : List of ip address and ports of the host the client is connecting to

        @type id_client     : int
        @type list_address  : list

    """
    def __init__(self, id_client):

        self.id_client = id_client
        self.list_address = Parser.get_backend_broker_list()
        p = Process(target=self.routine, args=(self.id_client,self.list_address))
        p.start()
        time.sleep(0.01)

    @staticmethod
    def routine(x,y):
         c = Client(x,y)
         c.generate()
         while(True):
             c.pull()
             print("#####################################")
             for x in c.pull_list:
                 print(x)
             print("######################################")
             time.sleep(3)

