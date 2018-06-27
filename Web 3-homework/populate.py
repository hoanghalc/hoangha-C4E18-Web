from models.service import Service
import mlab
from faker import Faker
from random import randint, choice
mlab.connect()

fake = Faker()


for i in range(20):
    print("Saving service",i + 1,"......")
    new_service = Service(
        name=fake.name(),
        yob=randint(1990,2000),
        gender=randint(0,1),
        height=randint(155,190),
        phone=fake.phone_number(),
        description = choice(["ngoan","ngon",'ngu',"dam dang"]),
        measurement = choice(['90,60,90',
                              '90,90,90',
                              '70,80,90']
        )                                   
    )

    new_service.save()