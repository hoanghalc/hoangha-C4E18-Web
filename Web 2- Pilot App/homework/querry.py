from module.service import Service
import mlab

mlab.connect()

id_to_find ="5b2ba505f9b057fb4c202b0f"

#Cach 1:
finder = Service.objects.get(id=id_to_find)
print(finder.name)

print('*' * 20)

#Cach 2:
finder = Service.objects.with_id(id_to_find) 
if finder is not None:
    # finder.delete()
    # print("Deleted")
    print(finder.address)
else:
    print("Service not found")