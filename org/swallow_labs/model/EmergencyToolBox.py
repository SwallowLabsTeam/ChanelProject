from org.swallow_labs.model.Broker import*
import socket
from org.swallow_labs.model.Capsule import *
from org.swallow_labs.tool.CapsulePriority import *
import hashlib


class EmergencyToolBox:

    def __init__(self):


        self.file_store = Parser().get_snapshot_param()


    def store(self,element_list, obj):
        date = time.ctime()
        adr = socket.gethostbyname(socket.gethostname())
        backend = str(obj.id_backend)
        frontend = str(obj.id_frontend)
        md5_data = str(str(date)+str(adr)+backend+frontend)




        a = {'date': date,
             'broker_info': {"adr":adr , "backend": backend,
                             "frontend":frontend}}

        a['msg_list']=[]
        for x in element_list:

             a['msg_list'].append(json.dumps(x.__dict__))





        for y in a['msg_list']:
            md5_data=md5_data+str(y)


        md5_hash = hashlib.md5(str(md5_data).encode("utf-8")).hexdigest()
        a["md5_hash"]=md5_hash

        with open(self.file_store+'/'+str(time.strftime("%Y%m%d"))+'_'+str(adr)+':'+backend+'**'+frontend+'.snp', "w") as json_file:
            json.dump(a, json_file)



    def snapshot(self, obj):
        element_list = obj.snapshot()
        self.store(element_list, obj)

    def reload(self,path):

        son_data = open(path).read()
        data = json.loads(son_data)
        data_check = str(str(data["date"])+str(data['broker_info']["adr"])+str(data['broker_info']['backend'])+str(data['broker_info']['frontend']))
        for y in data["msg_list"]:
            data_check = data_check+str(y)

        data_hash = hashlib.md5(str(data_check).encode("utf-8")).hexdigest()
        if str(data_hash)==data["md5_hash"]:

            li=[]
            for x in data["msg_list"]:
                y=json.loads(x)
                c=Capsule()
                c.set_id_receiver(y["id_receiver"])
                c.id_capsule=y["id_capsule"]
                c.set_payload(y["payload"])
                c.id_sender=y["id_sender"]
                c.set_priority(y["priority"])
                c.set_sending_date(y['sending_date'])
                c.set_status_capsule(y['status_capsule'])
                c.set_type(y['type'])
                li.append(c)

            b = Broker(data['broker_info']['frontend'], data['broker_info']['backend'])
            b.message_list = li
            print("Correct MD5 check")
            return (b)
        else:
            print("FATAL ERROR THE DATA IS CHANGED")
            return None











'''k=p.reload("/home/salmen/Fri Jun 17 12:07:06 2016_127.0.1.1:4442**4444.snp")
print("Reload Broker DONE with:")
print("id_backend: "+k.id_backend)
print("id_frontend: "+k.id_frontend)
print("Message liste:")
for x in k.message_list:
    print(x.print_capsule())'''


