import json


class ParserLogFile:

    def __init__(self, path):
        json_data = open(path).read()
        self.data = json.loads(json_data)

    def get_param_broker(self):

        param = [self.data['HOST'], self.data['PORT'], self.data['LEVEL_BROKER'], self.data['FACILITY_BROKER'], self.data['FORMAT'], "BROKER"]
        return param

    def get_param_client(self,id_client):
        param = [self.data['HOST'], self.data['PORT'], self.data['LEVEL_CLIENT'], self.data['FACILITY_CLIENT'], self.data['FORMAT'], id_client]
        return param




