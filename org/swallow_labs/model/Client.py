from org.swallow_labs.model.SocketClient import SocketClient
import queue as Q





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

    @param id_client : a client id
    @param list_address : List of ip address and ports of the host the client is connecting to
    @param sock_list: list of cnx socket used by the Client
    @param nbr_broker: Number of Brokers where the client is connecting to
    @param pull_list: List of message pulled by the client

    @ivar self.id_client : a client id
    @ivar list_address : List of ip address and ports of the host the client is connecting to
    @ivar sock_list: list of cnx socket used by the Client
    @ivar nbr_broker: Number of Brokers where the client is connecting to
    @ivar pull_list: List of message pulled by the client

    """
    cpt = 0

    def __init__(self,id_client,list_address ):

        self.id_client=id_client
        self.list_address=list_address
        self.sock_list=[]
        self.nbr_broker=len(list_address)
        self.pull_list=[]





    def generate(self):
        """

                DESCRIPTION
                ===========
                Method generate the Client communication stub (MultiSocket)
         """
        for i in range(self.nbr_broker):
            self.sock_list.append(SocketClient(self.id_client,self.list_address[i].adr,self.list_address[i].port))

    def push(self,capsule):

        """

                        DESCRIPTION
                        ===========
                        Method sending capsule for the appropriate broker

                        @param capsule : the capsule to send
        """

        self.sock_list[self.cpt].push(capsule)
        Client.cpt_inc()
        if Client.cpt == self.nbr_broker :
            Client.cpt_zero()

    def pull(self):

        """

                                DESCRIPTION
                                ===========
                               Method allowing the client to pull the messages that concern him from all Broker and sort them


        """

        for i in range(self.nbr_broker):
            self.pull_list=self.pull_list+self.sock_list[i].pull()
        self.tri()

    def tri(self):
        """

                         DESCRIPTION
                         ===========
                        Method that sort the pull_list


         """


        inter=[]
        aux=Q.PriorityQueue()
        for i in range(len(self.pull_list)):

           aux.put((self.pull_list[i].get_priority(),i))

        #self.pull_list=[]
        while not aux.empty():


            inter.append(self.pull_list[aux.get()[1]])

        self.pull_list=inter

    @staticmethod
    def cpt_inc():
        Client.cpt += 1
        return Client.cpt

    @staticmethod
    def cpt_zero():
        Client.cpt=0
        return Client.cpt