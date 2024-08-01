class engine:
    def __init__(self,  type):
        self.type = type
    def start(self):
        print("Engine is starting")
    def stop(self):
        print("Engine is stopping")
class wheel:
    def __init__(self,  type):
        self.type = type
    def start(self):
        print("Wheel is starting")
    def stop(self):
        print("Wheel is stopping")
class car:
    def __init__(self, engine, wheel):
        self.engine = engine
        self.wheel = wheel
    def start_car(self):
        self.engine.start()
        print("Car started")

e = engine("diesel")
w = wheel("alloy")
c = car(e, w)
c.start_car()
