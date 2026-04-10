class Student:
    #constructor
    def __init__(self,gender,name,age):
        self.gender = gender
        self.name = name
        self.age = age
        print("New Student added")
    #function to show task
    def print_message(self):
      print("name = ",self.name)
      print("age = ",self.age)
      print("gender = ",self.gender)
#create object
person1 = Student("male","Thamoghna",14)
person2 = Student("female","Thanishka",14)
person3 = Student("male","Rufus",14)
#call function to show task
person1.print_message()
print("----")
person2.print_message()
print("----")
person3.print_message()