class vechile:
    
    attr="car"

    def __init__(self, brand,model,fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        
    def color(self,paint):
        return "{} {} is an {} color car.".format(self.brand,self.model,paint)
    def modify(self):
        return "{} {} has modified".format(self.brand,self.model)
    

my_car = vechile("benz","s-class","diesel")
his_car = vechile("skoda","octavia vrs","petrol")
pentafox_car = vechile("toyota","innova crysta","diesel")

print(my_car.color("white"))
print(my_car.modify())
print(pentafox_car.color("white"))