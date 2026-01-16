#Intro to tuples

name = "Tanshi" #variable
names = ["Tanshi","Thamoghna","Rufus"]#list
names_dict = {"Thamoghna":14,
"Rufus":14,
"Tanshi":26}
print(name)
print(names)
print(names_dict)

student_details = ("Sam",59,"coding","basketball")
print(student_details)

address = ("85","Southern Perimeter Road","London","UK","England","TW7 5ZE")
print(address)

for i in address:
    print(i,end=" ")

print("\n")

door_number,road,area,state,country,postal_code = address
print(door_number)    

print(road)

print(area)

print(state)

print(country)

print(postal_code)