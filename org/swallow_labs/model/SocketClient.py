import zmq
import json
import socket
from contextlib import closing
import time
from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsuleType import CapsuleType



class SocketClient:
    """
    Class creating a SocketClient object:

    G{classtree}

    DESCRIPTION
    ===========
    Create a SocketClient

    RETURN
    ======
    Return a SocketClient

    @param id_client : a client id
    @param address : ip address of the host the client is connecting to
    @param port: port of the host the client is connecting to
    @ivar self.id_client : a client id
    @ivar self.address : ip address:server adresse the client is connecting to
    @ivar self.port : port of the host the client is connecting to
    @ivar self.socket: the socket enabling the connection

    """

    def __init__(self, id_client, address, port):
        """


        """
        # Initialize client
        self.id_client = id_client
        self.address = address
        self.port = port
        # Create a Context object to be able to call socket method
        context = zmq.Context(1)
        # Create a DEALER socket
        self.socket = context.socket(zmq.DEALER)
        # Assign an id to the client
        self.socket.setsockopt(zmq.IDENTITY, bytes(self.id_client,"utf8"))
        # Connect to the designed host
        self.socket.connect("tcp://" + self.address + ":" + self.port)

    # Method that check if the port server is open or not
    def CheckPort(self):
        """

        DESCRIPTION
        ===========
        Method check if the port server is open or not



        """
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((self.address, int(self.port))) == 0:
                return 1

            else:
                return 0

    # Method sending a message to an other client via the broker
    def push(self, capsule):
        """

        DESCRIPTION
        ===========
        Method providing a way for the client to send messages through the broker

        @param capsule : the capsule to send

        """
        if self.CheckPort():

            self.socket.send_json(json.dumps(capsule.__dict__))
        else:
            print("server closed")

    # Method allowing the client to pull the data concerning him
    def pull(self):
        """
        DESCRIPTION
        ===========
        Method allowing the client to pull the messages that concern him from the broker

        @rtype: List
        """
        if self.CheckPort():

            c = Capsule(self.id_client)
            c.set_type(CapsuleType.READY)
            self.socket.send_json(json.dumps(c.__dict__))
            message_list = []
            while True:
                j = self.socket.recv_json()
                p = json.dumps(j)

                c = Capsule(j=p)
                if c.get_type() == CapsuleType.END:
                    break
                else:
                    c.set_receiving_date(time.localtime())
                    message_list.append(c)
                    print("Let's talk about {}".format(json.dumps(c.__dict__)))
            return message_list

        else:

            return [None]
