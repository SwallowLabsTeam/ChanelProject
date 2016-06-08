import json
import time


class Capsule:
    """
        Class creating a capsule object:

        G{classtree}

        DESCRIPTION
        ===========
        Create a capsule

        RETURN
        ======
        Return a capsule

        @param id_sender:    Sender ID
        @param j:    Json object

        @type id_sender: int
        @type j: String

        @ivar self.id_sender:    Sender ID
        @ivar self.id_receiver:    Receiver ID
        @ivar self.payload:    Message wanted to send
        @ivar self.type:    Message type (PAYLOAD, READY, SENT, END)
        @ivar self.date:    Sending and receiving date(separated by *)
        @ivar self.status_capsule:    Capsule status(YES if read it and NO if still not read it by the broker)
        """
    def __init__(self, id_sender=None, j=None):
        """
            :

        """
        if j is None:
            self.id_sender = id_sender
            # By default the status of the capsule is not yet read by the broker
            self.status_capsule = "NO"
            # add to the capsule, date of sending
            self.date = time.strftime('%d/%m/%y %H:%M', time.localtime())
        else:
            self.__dict__ = json.loads(j)

    # Capsule getters

    def get_id_sender(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the sender ID

        """
        return self.id_sender

    def get_id_receiver(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the receiver ID

        """
        return self.id_receiver

    def get_payload(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the payload

        """
        return self.payload

    def get_status_capsule(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule status

        """
        return self.status_capsule

    def get_type(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the capsule type

        """
        return self.type

    def get_date(self):
        """

        DESCRIPTION
        ===========
        Method providing a way to get the time of sending and receiving of the capsule(separated by *)

        """
        return self.date

    # Capsule setters

    def set_id_receiver(self, id_receiver):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the receiver ID

        """
        self.id_receiver = id_receiver

    def set_payload(self, payload):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the payload

        """
        self.payload = payload

    def set_date(self, date):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the sending or receiving date

        """
        self.date = date

    def set_status_capsule(self, status_capsule):
        """

        DESCRIPTION
        ===========
        Method providing a way to set the capsule status

        """
        self.status_capsule = status_capsule

    def set_type(self, type):
        """

        DESCRIPTION
        ===========
        Method Setting capsule type

        """
        self.type = type



