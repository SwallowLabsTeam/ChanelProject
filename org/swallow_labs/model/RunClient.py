from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *
from multiprocessing import Process
from org.swallow_labs.model.CapsuleProcessor import CapsuleProcessor
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
        @param client       : the client stub

        @type id_client     : int
        @type list_address  : list
        @type client        : Client

    """

    def __init__(self, id_client):

        """
            DESCRIPTION
        ===========

        """

        self.id_client = id_client
        self.list_address = Parser.get_backend_broker_list()
        # Load global client param
       # global RR
        #RR = 5
        global client
        client = Client(self.id_client, self.list_address)
        # instantiate a Client
        p = Process(target=self.routine)
        p.start()
        time.sleep(0.01)
        # launch the routine method in a process


    def routine(self):

         """
            DESCRIPTION
        ===========
        Method that run a client stub and pull capsule in loop

         """
         client.generate()
         while (True):
             # loop for pull
             client.pull()
             # client pull
             for x in client.pull_list:
                 print(x.print_capsule())
                 t = CapsuleProcessor(x)
                 # instantiate a CapsuleProcessor that will treat capsule
                 t.treat()
                 # treat capsule
                 x.my_logger.log_treated_capsule(x)
                 # log that the capsule was treated
                 client.pull_list.pop(0)
                 # pop the treated capsule from the pull_list
             # treat pull_list capsule
             time.sleep(0.5)



