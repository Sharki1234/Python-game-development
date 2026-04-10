#make class
class House:
    #make constructor
    def __init__(self,location,area):
        #make properties
        self.location = location
        self.area = area
        print("New House added")
    #make method/task
    def make_house(self):
        print("Location:",self.location)
        print("Area:",self.area)
house1 = House("south",1489)
house1.make_house()