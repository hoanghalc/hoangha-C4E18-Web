
from models.river_ex import River
import mlab

mlab.connect()

river_in_Africa = River.objects(continent = "Africa")

for river in river_in_Africa:
    print(river.name)
    print(river.length)
    print("-" * 20)

print("*" * 30)

river_less_than_1000 = River.objects(continent ="S. America",length__lt = 1000)
for river in river_less_than_1000:
    print(river.name)
    print(river.length)
    print("-" * 20)


