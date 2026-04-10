#make vehicle
class Vehicle:
    #constructor
    def __init__(self,material,power_source):
        self.material = material
        self.power_source = power_source
        print("New Vehicle added")
    def make_vehicle(self):
        print("Material:",self.material)
        print("Power_Source:",self.power_source)
vehicle1 = Vehicle("Ultra Refined Pure Wakandan Vibranium Retrofitted with Ultrasonic Dampeners","Ultra Refined Pure Wakandan Vibranium Energy Core Retrofitted with Ultrasonic Dampeners")
vehicle1.make_vehicle()