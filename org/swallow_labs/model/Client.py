from org.swallow_labs.model.SocketClient import SocketClient
import queue as Q
import logging
import logging.handlers


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

        @param id_client    : a client id
        @param list_address : List of ip address and ports of the host the client is connecting to

        @type id_client     : int
        @type list_address  : list
    """
    cpt = 0

    def __init__(self, id_client, list_address):
        self.logger = logging.getLogger('Client {}'.format(self.id_client))
        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.handlers.SysLogHandler(address=('192.168.1.250', 514), facility='local1')
        # fh = logging.FileHandler('broker.log')
        self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        self.id_client = id_client
        self.list_address = list_address
        self.sock_list = []
        self.nbr_broker = len(list_address)
        self.pull_list = []

    def generate(self):
        """
            DESCRIPTION
            ===========
            Method generate the Client communication stub (MultiSocket)
         """
        for i in range(self.nbr_broker):
            self.sock_list.append(SocketClient(str(self.id_client),
                                               str(self.list_address[i].address),str(self.list_address[i].port)))

    def push(self, capsule):

        """
            DESCRIPTION
            ===========
            Method sending capsule for the appropriate broker

            @param capsule : the capsule to send
        """

        self.sock_list[self.cpt].push(capsule)
        self.logger.debug('sent : {}'.format(capsule.__dict__))
        Client.cpt_inc()
        if Client.cpt == self.nbr_broker:
            Client.cpt_zero()
        return 1

    def pull(self):

        """
            DESCRIPTION
            ===========
            Method allowing the client to pull the messages that concern him from all Broker and sort them
        """

        for i in range(self.nbr_broker):
            self.pull_list = self.pull_list+self.sock_list[i].pull()
        self.tri()
        for x in self.pull_list:
            self.logger.debug('messages retrieved {}'.format(x.__dict__))
        return 1

    def tri(self):
        """
            DESCRIPTION
            ===========
            Method that sort the pull_list
        """

        inter = []
        aux = Q.PriorityQueue()
        for i in range(len(self.pull_list)):

            aux.put((self.pull_list[i].get_priority(),i))

        while not aux.empty():
            inter.append(self.pull_list[aux.get()[1]])
        self.pull_list = inter

    @staticmethod
    def cpt_inc():
        """
            DESCRIPTION
            ===========
            Method incrementing the counter
        """
        Client.cpt += 1
        return Client.cpt

    @staticmethod
    def cpt_zero():
        """
            DESCRIPTION
            ===========
            Method reinitialising the counter
        """
        Client.cpt = 0
        return Client.cpt
