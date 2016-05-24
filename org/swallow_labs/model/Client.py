import zmq
import json
from org.swallow_labs.model.Capsule import Capsule


class Client:
    """
        Class creating a client object:

        G{classtree}

        DESCRIPTION
        ===========
            Create a client

        RETURN
        ======
        Return a client

        PARAMETERS
        ==========
        @param id_client : a client id
        @param connection : ip address:port of the host the client is connecting to
        @ivar self.id_client : a client id
        @ivar self.connection : ip address:port of the host the client is connecting to
        @ivar self.socket: the socket enabling the connection

    """

    def __init__(self, id_client, connection):
        """
            :

        """
        # Initialize client
        self.id_client = id_client
        self.connection = connection
        # Create a Context object to be able to call socket method
        context = zmq.Context(1)
        # Create a DEALER socket
        self.socket = context.socket(zmq.DEALER)
        # Assign an id to the client
        self.socket.setsockopt(zmq.IDENTITY, bytes(self.id_client, 'utf8'))
        # Connect to the designed host
        self.socket.connect("tcp://"+self.connection)

    # Method sending a message to an other client via the broker
    def push(self, capsule):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way for the client to send messages through the broker

            PARAMETERS
            ==========
            @param capsule : the capsule to send

        """
        self.socket.send_json(json.dumps(capsule.__dict__))

    # Method allowing the client to pull the data concerning him
    def pull(self):
        """
            :
            DESCRIPTION
            ===========
            Method allowing the client to pull the messages that concern him from the broker
        """
        c = Capsule(self.id_client)
        c.set_type("READY")
        self.socket.send_json(json.dumps(c.__dict__))
        message_list = []
        while True:
            j = self.socket.recv_json()
            p = json.dumps(j)

            c = Capsule(j=p)
            if c.get_type() == "END":
                break
            else:
                message_list.append(c)
                print("Let's talk about {}".format(json.dumps(c.__dict__)))
        return message_list
