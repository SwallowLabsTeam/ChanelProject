import zmq
import json


class Client:
    """G{classtree}
    Class defining a client characterised by:
    @param id_client : a client id
    @param connection : ip address:port of the host the client is connecting to
    @param socket: the socket enabling the connection"""

    def __init__(self, id_client, connection):
        """This method is called upon instantiating the Client Class
        @param id_client : a client id
        @param connection : ip address:port of the host the client is connecting to"""
        # Initialize client
        self.id_client = id_client
        self.connection = connection
        # Create a Context object to be able to call socket method
        context = zmq.Context(1)
        # Create a DEALER socket
        self.socket = context.socket(zmq.DEALER)
        # Assign an id to the client
        self.socket.setsockopt(zmq.IDENTITY, self.id_client)
        # Connect to the designed host
        self.socket.connect("tcp://"+self.connection)

    # Method sending a message to an other client via the broker
    def push(self, id_receiver, payload):
        """This method provides a way for the client to send messages through the broker
        @param id_receiver : id of the client that shall receive the message
        @param payload : the data that s being transferred"""
        self.socket.send_multipart([id_receiver, bytes(payload, 'utf8')])

    # Method allowing the client to pull the data concerning him
    def pull(self):
        """this method helps the client pull the messages that concern him from the broker"""
        self.socket.send(b'READY')
        while True:
            msg = self.socket.recv_multipart()
            if msg[0] == b"END":
                break
            else:
                print("Let's talk about %s" % msg[0])
                data = json.loads(msg[0].decode('utf8'))
                print(json.dumps(data, indent=4))

