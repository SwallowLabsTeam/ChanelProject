import zmq


class Broker:
    """class defining a broker characterised by :
    - idFrontEnd : port number for the back-end socket
    - idBackEnd :  port number for the front-end socket
    - frontEnd : front-end socket
    - backEnd : back-end socket"
    - poller : A stateful poll object"
    - MessageList : a list containing the messages received from the clients other than the Ready message"""
    def __init__(self, id_frontend, id_backend):
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
        self.messageList = []

    def clean(self):
        i = 0
        while i < len(self.messageList):
            if self.messageList[i][0] == b"SENT":
                print(self.messageList.pop(i))
                i -= 1
            i += 1

    def start(self):

        while True:
            # Convert the return of the poll method into a dictionary
            socks = dict(self.poller.poll())
            # if the the argument iss true, it means that a message is received on the front-end socket
            if socks.get(self.frontend) == zmq.POLLIN:
                # receive message into the variable message
                message = self.frontend.recv_multipart()
                print(message)
                # Since this is a multipart message The first part will contain the receive id
                # The second part will contain the payload
                # if the payload is equal to READY (b stands for bytes conversion)
                if message[1] == b"READY":
                    # We get into the loop to check if the client who sent the ready message
                    # has any messages for him stored into the messageList variable
                    for k in range(len(self.messageList)):
                        if self.messageList[k][0] == message[0]:
                            self.frontend.send_multipart(self.messageList[k])
                            self.messageList[k][0] = b"SENT"
                    self.frontend.send_multipart([message[0], b"END"])

                else:
                    # If the message is anything other then the ready message
                    # Store it into the messageList
                    self.messageList.append([message[1], message[2]])
            # the back-end works the same as the front-end
            if socks.get(self.backend) == zmq.POLLIN:
                message = self.backend.recv_multipart()
                print(message)

                if message[1] == b"READY":
                    for k in range(len(self.messageList)):
                        if self.messageList[k][0] == message[0]:
                            self.backend.send_multipart(self.messageList[k])
                            self.messageList[k][0] = b"SENT"
                    self.backend.send_multipart([message[0], b"END"])
                else:
                    self.messageList.append([message[1], message[2]])

            if len(self.messageList) > 0:
                self.clean()



