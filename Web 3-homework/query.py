from models.service import Service
import mlab

mlab.connect()

#Delete all document from collection
all_service = Service.objects().delete()

