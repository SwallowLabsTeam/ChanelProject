import json


class ParserLogFile:

    def __init__(self, path):
        json_data = open(path).read()
        self.data = json.loads(json_data)

    def get_param_log_broker(self):

        param = [self.data['log_param']['host'], self.data['log_param']['port'], self.data['log_param']['level_broker'],
                 self.data['log_param']['facility_broker'], self.data['log_param']['format'], "Broker"]
        return param

    def get_param_log_client(self):
        param = [self.data['log_param']['host'], self.data['log_param']['port'], self.data['log_param']['level_client'],
                 self.data['log_param']['facility_client'], self.data['log_param']['format'], "Client"]
        return param

    def get_param_log_capsule(self):
        param = [self.data['log_param']['host'], self.data['log_param']['port'], self.data['log_param']['level_capsule'],
                 self.data['log_param']['facility_capsule'],
                 self.data['log_param']['format'], "Capsule"]
        return param




