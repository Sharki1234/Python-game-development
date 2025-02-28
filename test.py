class Student:
    name = "Tiffany"
    role = 0
    score = 0
    def change_role(self):
        new = int(input("role"))
        return(new)
    def change_score(self):
         new2 = int(input("score"))
         return(new2)

person = Student()
person.role = person.change_role()
print(person.role)