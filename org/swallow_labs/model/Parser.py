import json
from jsonschema import validate
import ast


class BrokerData:
    """
        Class creating a BrokerData object
        G{classtree}
        DESCRIPTION
        ===========
            Class containing the necessary data about the brokers to be able to initialize the clients

        @param address:    The Broker's ip address
        @param port:    port number

        @type address: string
        @type port: int
    """
    def __init__(self, address, port):
        self.address = address
        self.port = port


class Parser:
    """
        Class creating a Parser object
        G{classtree}
        DESCRIPTION
        ===========
            Class that s handeling the parsing of the json files in order to store data and make it available for use
            by other components

        @param client_path:    path of the json file containing the client infos
        @param broker_path:    path of the json file containing the brokers infos

        @type client_path: string
        @type broker_path: string
    """
    def __init__(self, client_path, broker_path):
        json_data = open(client_path).read()
        self.client_id = json.loads(json_data)
        json_data = open(broker_path).read()
        self.data = json.loads(json_data)
        json_data = open('schema').read()
        schema = ast.literal_eval(json_data)
        self.broker_list = []
        try:
            validate(self.data, schema)
            if self.client_id >= 10:
                for i in range(len(dict(self.data)['ip_add'])):
                    self.broker_list.append(BrokerData(dict(self.data)['ip_add'][i], dict(self.data)['back_end'][i]))
            else:
                    for i in range(len(dict(self.data)['ip_add'])):
                        self.broker_list.append(BrokerData(dict(self.data)['ip_add'][i], dict(self.data)['front_end'][i]))
        except:
            print("Your json file is INVALID")

    def get_client_id(self):
        return self.client_id

    def get_broker_list(self):
        return self.broker_list


