import json
from jsonschema import validate
from jsonschema import *
import ast
from org.swallow_labs.model.BrokerData import BrokerData


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
    def __init__(self, broker_path, client_path):
        json_data = open('schema').read()
        schema = ast.literal_eval(json_data)
        if broker_path is not None and client_path is not None:
            json_data = open(client_path).read()
            self.client_id = json.loads(json_data)
            json_data = open(broker_path).read()
            self.data = json.loads(json_data)
            self.broker_list = []
            try:
                validate(self.data, schema)
                if self.client_id >= 10:
                    for i in range(len(dict(self.data)['net_param']['ip_add'])):
                        self.broker_list.append(BrokerData(dict(self.data)['net_param']['ip_add'][i],
                                                           dict(self.data)['net_param']['back_end'][i]))
                else:
                        for i in range(len(dict(self.data)['net_param']['ip_add'])):
                            self.broker_list.append(BrokerData(dict(self.data)['net_param']['ip_add'][i],
                                                               dict(self.data)['net_param']['front_end'][i]))
            except:
                print("Your json file is INVALID")
        else:
            json_data = open(broker_path).read()
            self.data = json.loads(json_data)
            try:
                validate(self.data, schema)
            except:
                print("Your json file is INVALID")

    def get_param_log_broker(self):

        param = [self.data['log_param']['host'], self.data['log_param']['port'], self.data['log_param']['level_broker'],
                 self.data['log_param']['facility_broker'], self.data['log_param']['format'], "Broker"]
        return param

    def get_param_log_client(self):
        param = [self.data['log_param']['host'], self.data['log_param']['port'], self.data['log_param']['level_client'],
                 self.data['log_param']['facility_client'], self.data['log_param']['format'], "Client"]
        return param

    def get_param_log_capsule(self):
        param = [self.data['log_param']['host'], self.data['log_param']['port'],
                 self.data['log_param']['level_capsule'],
                 self.data['log_param']['facility_capsule'],
                 self.data['log_param']['format'], "Capsule"]
        return param
    def get_client_id(self):
        return self.client_id

    def get_broker_list(self):
        return self.broker_list


