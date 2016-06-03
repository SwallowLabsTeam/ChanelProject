from org.swallow_labs.model.Parser import *
from org.swallow_labs.model.Client import *
from org.swallow_labs.model.Launcher import *

json_data = open('json example').read()
data = json.loads(json_data)
json_data = open('schema').read()
schema = ast.literal_eval(json_data)
validate(data, schema)  # in case the json data isn't valid this function will throw an exception.

parser = Parser('client', 'json example')
client = Client(parser.get_client_id(), parser.get_broker_list())
print(client)
print("client id: {}".format(client.id_client))
for x in client.list_address:
    print("le client est connecté sur le broker de port: {} et addresse: {}".format(x.port, x.address))

broker_launcher = Launcher('json example')
