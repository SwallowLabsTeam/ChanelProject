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
    def send_capsule(self,x):
        SendProcessor.send_in_sending_list(x)
        SendProcessor.send(self.cpl,x)
    @staticmethod
    def send_in_sending_list(y):
        for x in sending_list:
            if SendProcessor.verify_tts(x):
                SendProcessor.send(x,y)

    @staticmethod
    def send(x,y):
        if x.get_priority() == CapsulePriority.BOOKING_MSG:
            sending_list.append(x)

        y.push(x)


    @staticmethod
    def verify_tts(x):
        """

        @param x: Verify tts Capsule
        @return: if the sending time + tts is upper to current time retun True else return false
        @type x: Capsule
        @rtype: bool
        """
        w = datetime.datetime.strptime(x.get_sending_date(), "%a %b %d %H:%M:%S %Y")
        if (w+ datetime.timedelta(0, x.get_tts())>=datetime.datetime.now()):
            return False
        else:
            return True