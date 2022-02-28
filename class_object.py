class vechile:
    
    attr="car"

    def __init__(self, brand,model,fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

my_car = vechile("benz","s-class","diesel")
his_car = vechile("skoda","octavia vrs","petrol")
pentafox_car = vechile("toyota","innova crysta","diesel")

print("my car is a {} {}, {} variant".format(my_car.brand,my_car.model,my_car.fuel))
print("his car is a {} {}, {} variant".format(his_car.brand,his_car.model,his_car.fuel))
print("pentafox car is a {} {}, {} variant".format(pentafox_car.brand,pentafox_car.model,pentafox_car.fuel))

