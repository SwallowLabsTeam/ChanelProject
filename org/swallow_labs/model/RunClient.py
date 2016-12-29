from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *
from multiprocessing import Process
from org.swallow_labs.model.CapsuleProcessor import CapsuleProcessor
import time
import zmq
from org.swallow_labs.model.BrokerEventManager import *
import org.swallow_labs.model.SendProcessor
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

    def __init__(self, id_client,id_event):

        """
            DESCRIPTION
        ===========

        """

        self.id_client = id_client
        self.id_event = id_event
        self.list_address = Parser.get_backend_broker_list()
        # Load global client param
       # global RR
        #RR = 5
        self.event=BrokerEventManager(self.id_event)
        global client
        client = Client(self.id_client, self.list_address)
        global client2
        client2 = Client(22, self.list_address)
        client2.generate()
        # instantiate a Client
        p = Process(target=self.routine)
        p.start()
        time.sleep(0.01)
        p1 = Process(target=self.eve())
        p1.start()
        time.sleep(0.01)
        p.join()
        p1.join()
        # launch the routine method in a process

    def eve(self):
        self.event.start(client2)
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

                 if(x.get_ACK=="YES"):
                     pld=x.get_payload()
                     for w in org.swallow_labs.model.SendProcessor.sending_list:
                         print("wwwwwww",w)
                         if(w.get_id_sender()==pld["id"]):
                             org.swallow_labs.model.SendProcessor.sending_list.remove(w)
                 else:
                     t = CapsuleProcessor(x)
                     print("lissst ",org.swallow_labs.model.SendProcessor.sending_list)
                     # instantiate a CapsuleProcessor that will treat capsule
                     y = t.verif_msg()
                     print("yyy ", y)
                     if (y == None):
                         print('capsule verif false')
                         org.swallow_labs.model.SocketClient.my_logger.log_sendACK_verif(
                             str(x.id_capsule), str(
                                 org.swallow_labs.model.RunClient.client.id_client))
                     else:
                         t.treat(y)

                     # instantiate a CapsuleProcessor that will treat capsule
                     # t.treat()
                     # treat capsule
                     x.my_logger.log_treated_capsule(x)
                     # log that the capsule was treated
                     client.pull_list.pop(0)
                     # pop the treated capsule from the pull_list
                 # treat pull_list capsule
             time.sleep(3)
             print("lissst ", org.swallow_labs.model.SendProcessor.sending_list)
             print("ok")







