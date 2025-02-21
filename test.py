class Student:
    name = "Stephanie"
    def test(self):
        print(15)


person = Student()
p2 = Student()
p2.name = "radish"
print(person.name)
p2.test()