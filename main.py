import random

class VehicleFactory:
    @staticmethod
    def create_vehicle():
        vehicle_type = random.choice(['Car', 'Truck', 'Boat'])
        make = random.choice(['Ford', 'Toyota', 'Honda'])
        model = random.choice(['ModelX', 'ModelY', 'ModelZ']) # Simplified for this example
        year = random.randint(1990, 2022)
        weight = random.randint(1000, 3000)

        if vehicle_type == 'Car':         ##Instantiate the objects here
            return (vehicle_type, make, model, year, weight, "Beep!Beep!")
        elif vehicle_type == 'Truck':
            return (vehicle_type, make, model, year, weight, "HOOONK!")
        else:
            return (vehicle_type, make, model, year, weight, "BWORRRRRRNK!")

def process_vehicles(vehicles):
    for items in vehicles:
        print(items)
    return
   #for each Car, Boat or other, print its contents and make it honk




# Testing
vehicle_list = [VehicleFactory.create_vehicle() for _ in range(5)] #<- what does this do? It makes a list is what it does
process_vehicles(vehicle_list)