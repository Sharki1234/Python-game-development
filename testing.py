classroom = {}
while True:
    print("1.add name")
    print("2.edit age")
    print("3.delete")
    choice= int(input("what do you want to do?"))
    if choice == 1:
        name_add = input("name?")
        age_add = int(input("age?"))
        classroom[name_add]=age_add
    elif choice == 2:
        name_edit = input("name of change you want to change")
        if name_edit not in classroom:
            print("name doesn't exist")
        else:
            age_edit = int(input("age for edit?"))
            classroom[name_edit] = age_edit
    elif choice == 3:
        delete = input("what do you want to delete?")
        #classroom.pop(delete)
        del classroom[delete]
    print(classroom)
        