
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


class Penguin(Bird):

    def __init__(self):
       
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")
        

class Parrot(Bird):
    def __init__(self):
        super().__init__()
        print("Parrot is ready")
    def whoisThis(self):
        print("Parrot")
    def fly(self):
        print("fly faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
print("--------------------------")
peggy = Parrot()
peggy.whoisThis()
peggy.swim()
peggy.fly()
print("--------------------------")
peggy = Bird()
peggy.whoisThis()
peggy.swim()
