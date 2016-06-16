"Script to create 2 clients and log the operation "

from org.swallow_labs.model.Client import Client
from org.swallow_labs.model.Parser import *

p = Parser('../conf/Configuration.json', 'client')
id_client = p.get_client_id()
connexions = p.get_broker_list()
client = Client(id_client, connexions)
print("Client launched")