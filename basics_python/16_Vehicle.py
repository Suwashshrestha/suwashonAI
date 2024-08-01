class vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        print("Driving the ", self.make, ", ", self.model,)
class car(vehicle):
    def drive(self):
        print("Driving the ", self.make, ", ", self.model, " car")
v = vehicle("Toyota", "mercedes")
v.drive()
c = car("hundya", "mercedes")
c.drive()
