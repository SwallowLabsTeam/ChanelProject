from org.swallow_labs.model.Capsule import Capsule
from org.swallow_labs.tool.CapsuleSort import CapsuleSort
from org.swallow_labs.model.LdapParam import *
import os

class CapsuleProcessor:

    """
        Class creating a CapsuleProcessor object
        G{classtree}
        DESCRIPTION
        ===========
        Class that treat capsule

        @param cpl    : The capsule that will be treated


        @type cpl     : Capsule

    """
    ldap_param = LdapParam()
    # Static variable that contain ldap connexion param
    def __init__(self, cpl):
        # initialize the capsule  that will be treated
        self.cpl = cpl


    def treat(self):
        """
            DESCRIPTION
            ===========
            Method that treat a capsule
        """
        if self.cpl.get_sort() == CapsuleSort.LDAP_ADD_MSG:
        # Test the sort of capsule
            self.treat_ldap_add_msg()
            # Run the method that treat the LDAP_ADD_MSG capsule

        elif self.cpl.get_sort() == CapsuleSort.LDAP_MOD_MSG:
        # Test the sort of capsule
            self.treat_ldap_mod_msg()
            # Run the method that treat the LDAP_MOD_MSG capsule

        elif self.cpl.get_sort() == CapsuleSort.LDAP_DEL_MSG:
        # Test the sort of capsule
            self.treat_ldap_del_msg()
            # Run the method that treat the LDAP_DEL_MSG capsule

    def treat_ldap_add_msg(self):
        """
            DESCRIPTION
            ===========
            Method that treat a LDAP_ADD_MSG capsule
        """
        pld = self.cpl.get_payload()
        # Get capsule payload
        add_file = 'ldap_add_file.ldif'
        # Specify the name of file that contain entry information
        self.ldap_file_creator(add_file,pld)
        # Creation of the ldap file using capsule payload information
        admin=self.ldap_param.admin
        password=self.ldap_param.password
        # Load ldap param
        os.system("ldapadd  -h 10.10.10.2  -D " + '"'+str(admin)+'"' + " -w "+ password+ " -f ./" + str(add_file))
        # execute the ldap command that will add the new entry in the ldap tree using ldap_add_file.ldif
        os.remove("./"+str(add_file))
        # delete ldap_add_file

    def treat_ldap_mod_msg(self):
        """
            DESCRIPTION
            ===========
            Method that treat a LDAP_MOD_MSG capsule
        """
        pld = self.cpl.get_payload()
        # Get capsule payload
        mod_file = 'ldap_mod_file.ldif'
        # Specify the name of file that contain the modification information
        self.ldap_file_creator(mod_file, pld)
        # Creation of the ldap file using capsule payload information
        self.ldap_file_creator(mod_file, pld)
        # Creation of the ldap file using capsule payload information
        admin = self.ldap_param.admin
        password = self.ldap_param.password
        # Load ldap param
        os.system("ldapmodify  -h 10.10.10.2  -D " + '"' + str(admin) + '"' + " -w " + password + " -f ./" + str(mod_file))
        # execute the ldap command that will modify the entry using ldap_mod_file.ldif
        os.remove("./" + str(mod_file))
        # delete ldap_mod_file

    def treat_ldap_del_msg(self):
        """
            DESCRIPTION
            ===========
            Method that treat a LDAP_DEL_MSG capsule
        """
        pld=self.cpl.get_payload()
        # Get capsule payload
        entry='"'+str(pld["dn"])+'"'
        # get the dn of entry that will be deleted
        admin = self.ldap_param.admin
        password = self.ldap_param.password
        # Load ldap param
        os.system("ldapdelete -h 10.10.10.2 -D "+ '"' + str(admin) + '"' + " -w " + password + " -f ./"+ entry )
        # execute the ldap command that will delete the entry

    @staticmethod
    def ldap_file_creator(file, pld):

        """
            DESCRIPTION
            ===========
            This method create file that contain ldap entry information
            @param file: the file name
            @param pld: capsule payload that will be copied in the file

            @type file: str
            @type pld : dict
        """
        f = open(file, 'w')
        for h in pld["att"]:
            if type(pld[str(h)]) == list:
                for k in pld[str(h)]:
                    f.write(h + ":" + k + "\n")
            else:
                f.write(h + ':' + pld[str(h)] + "\n")
        # write in the file the capsule payload that contains information about the new ldap entry
        f.close()



