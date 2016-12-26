from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsuleSort import CapsuleSort
from org.swallow_labs.model.LdapParam import *
import os
from org.swallow_labs.model.Client import *
from org.swallow_labs.model.CapsuleACK import *
from org.swallow_labs.tool.CapsulePriority import *
import org.swallow_labs.model.RunClient
import org.swallow_labs.model.SocketClient
from subprocess import *
import datetime

class SendProcessor:

    """
        Class creating a SendProcessor object
        G{classtree}
        DESCRIPTION
        ===========
        Class that treat capsule

        @param cpl    : The capsule that will be sent


        @type cpl     : Capsule

    """

    #get Brokers param
    global sending_list
    sending_list = []
    #

    def __init__(self, cpl):
        """
                :

        """
        self.cpl = cpl
        # initialize the capsule  that will be sent
    def send_capsule(self):
        self.send_in_sending_list()
        self.send(self.cpl)
    def send_in_sending_list(self):
        for x in SendProcessor.sending_list:
            if(self.verify_tts(x)):
                self.send(x)


    def send(self,x):
        if self.cpl.get_priority() == CapsulePriority.BOOKING_MSG:
            SendProcessor.sending_list.append(x)

        org.swallow_labs.model.RunClient.Client.push(x)

    def verify_tts(self,x):
        """

        @param x: Verify tts Capsule
        @return: if the sending time + tts is upper to current time retun True else return false
        @type x: Capsule
        @rtype: bool
        """
        if (x.get_sending_date()+ datetime.timedelta(0, x.get_tts())>=datetime.datetime.utcnow()):
            return False
        else:
            return True