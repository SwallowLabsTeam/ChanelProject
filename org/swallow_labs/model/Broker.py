import zmq
from org.swallow_labs.model.Capsule import Capsule
import json


class Broker:
    """
    Class creating a broker object

    G{classtree}

    DESCRIPTION
    ===========
    Create a broker

    RETURN
    ======
    Return a broker

    @param id_frontend:    port number for the front-end socket
    @param id_backend:    port number for the back-end socket
    @ivar self.frontend:    front-end socket
    @ivar self.backend:    back-end socket
    @ivar self.poller:    A stateful poll object
    @ivar self.message_list:    a list containing the messages received from the clients
                                other than the Ready message
    @type id_frontend: int
    @type id_backend: int

    """
    def __init__(self, id_frontend, id_backend):
        """


        """
        self.id_frontend = id_frontend
        self.id_backend = id_backend
        # Prepare context and sockets
        # Create a Context object to be able to call socket method
        context = zmq.Context()
        # Create a ROUTER socket for front-end connections
        self.frontend = context.socket(zmq.ROUTER)
        # Create a ROUTER socket for back-end connections
        self.backend = context.socket(zmq.ROUTER)
        # Bind front-end socket
        self.frontend.bind("tcp://*:" + str(self.id_frontend))
        # bind back-end socket
        self.backend.bind("tcp://*:" + str(self.id_backend))
        # Initialize poll set
        # Create a Poller object to detect the active sockets at a given time
        self.poller = zmq.Poller()
        # Register the front-end and back-end sockets into the poller
        self.poller.register(self.frontend, zmq.POLLIN)
        self.poller.register(self.backend, zmq.POLLIN)

    def clean(self):
        """
        DESCRIPTION
        ===========
        Method cleaning the message_list attribute of the broker by removing the messages that were sent
        """
        i = 0
        while i < len(self.message_list):
            if self.message_list[i].get_status_capsule() == "YES":
                self.message_list.pop(i)
                i -= 1
            i += 1

    def send(self, client_id, end):
        """
        DESCRIPTION
        ===========
            This method sends the capsules that contain the receiver id matching the receiver id received as parameter
            on the specified end

        @param client_id: id of the client to whom the message is sent
        @param end: this may take self.backend or self.backend
        @type client_id: string
        @type end : socket
        """
        for k in range(len(self.message_list)):
            if self.message_list[k].get_id_receiver() == client_id and self.message_list[k].get_status_capsule() != "YES":
                end.send_multipart([bytes(client_id, 'utf8'), bytes(json.dumps(self.message_list[k].__dict__), 'utf8')])
                self.message_list[k].set_status_capsule("YES")
        c = Capsule(0)
        c.set_type("END")
        end.send_multipart([bytes(client_id, 'utf8'), bytes(json.dumps(c.__dict__), 'utf8')])

    @staticmethod
    def parse(b_client_id, b_capsule):
        """
        DESCRIPTION
        ===========
        Method converting the b_client_id into a string and the b_capsule into a Capsule object
        @param b_client_id:    client id in bytes format
        @param b_capsule:   capsule in bytes format
        @return: return a list containing the client id as a string and the Capsule object
        @rtype: List
        @type b_client_id: Bytes
        @type b_capsule: Bytes
        """
        client_id = b_client_id.decode('utf8')
        c_recv = Capsule(j=json.loads(b_capsule.decode('utf8')))
        return[client_id, c_recv]

    def start(self):
        """

        DESCRIPTION
        ===========
        Method describing the behaviour of the broker it is the main loop in which he receives messages
        and forwards them to the appropriate peer
        """
        self.message_list = []
        while True:

            # Convert the return of the poll method into a dictionary
            socks = dict(self.poller.poll())
            # if the the argument iss true, it means that a message is received on the front-end socket
            if socks.get(self.frontend) == zmq.POLLIN:

                # receive client id and capsule as bytes
                b_client_id, b_capsule = self.frontend.recv_multipart()
                print(b_capsule)
                client_id, c_recv = Broker.parse(b_client_id, b_capsule)
                # Since this is a multipart message The first part will contain the receive id
                # The second part will contain the payload
                # if the payload is equal to READY (b stands for bytes conversion)
                if c_recv.get_type() == "READY":
                    # We get into the loop to check if the client who sent the ready message
                    # has any messages for him stored into the message_list variable
                    self.send(client_id, self.frontend)
                else:
                    # If the message is anything other then the ready message
                    # Store it into the messageList
                    self.message_list.append(c_recv)
            # the back-end works the same as the front-end
            if socks.get(self.backend) == zmq.POLLIN:

                # receive client id and capsule as bytes
                b_client_id, b_capsule = self.backend.recv_multipart()
                client_id, c_recv = Broker.parse(b_client_id, b_capsule)

                if c_recv.get_type() == "READY":
                    self.send(client_id, self.backend)
                else:
                    self.message_list.append(c_recv)

            if len(self.message_list) > 0:
                self.clean()



