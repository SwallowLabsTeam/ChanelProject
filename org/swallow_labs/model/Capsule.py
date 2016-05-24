import json


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

        PARAMETERS
        ==========
        @param id_sender:    Sender ID
        @param id_receiver:    Receiver ID
        @param payload:    Message wanted to send
        @param type:    Message type
        @param date:    creation, sent and received date(the sens from the left to right separated by *)
        @param status_capsule:    capsule status(yes if road it and no if still not road it by the broker)

        """
    def __init__(self, id_sender=None, j=None):
        """
            :

        """
        if j is None:
            self.id_sender = id_sender
        else:
            self.__dict__ = json.loads(j)

    # Capsule setters
    def set_id_sender(self, id_sender):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to set the sender ID

        """
        self.id_sender = id_sender

    def set_id_receiver(self, id_receiver):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to set the receiver ID

        """
        self.id_receiver = id_receiver

    def set_payload(self, payload):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to set the payload

        """
        self.payload = payload

    def set_date(self, date):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to get the creaction, sent and received date

        """
        self.date = date

    def set_status_capsule(self, status_capsule):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to get the creation, sent and received date

        """
        self.status_capsule = status_capsule

    def set_type(self, type):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to set the capsule type

        """
        self.type = type

    # Capsule getters
    def get_id_receiver(self):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to get the receiver ID

        """
        return self.id_receiver

    def get_status_capsule(self):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to get the capsule status

        """
        return self.status_capsule

    def get_type(self):
        """
            :
            DESCRIPTION
            ===========
            Method providing a way to get the capsule type

        """
        return self.type

