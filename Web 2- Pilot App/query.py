from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()
# first_service = all_service[0]

# print(first_service.height)

id_to_find = "5b2ba3ebf9b057fb06887435"

# hera = Service.objects.get(id = id_to_find) #Cách 1: 
# hero = Service.objects(id = id_to_find) #Cách 2
service = Service.objects.with_id(id_to_find)

if service is not None:
    # hera.delete()
    # print('Deleted')
    print(service.to_mongo())
    service.update(set__yob=1991)  #Update thong tin cua ID
    service.reload()    #Update thông tin từ database
else:
    print('Service not found')

print(service.to_mongo())  #In ra toan bo thong tin cua ID 
