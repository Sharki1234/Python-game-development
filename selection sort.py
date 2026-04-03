import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(1,100)
num4 = random.randint(1,100)
num5 = random.randint(1,100)
myselection = [num1,num2,num3,num4,num5]
total = len(myselection)
for i in range(total-1):
    smallest_index = i
    for j in range(i+1,total):
        if myselection[j]<myselection[smallest_index]:
            smallest_index = j
    minimum_value = myselection.pop(smallest_index)
    myselection.insert(i,minimum_value)
print(f"ascending order = {myselection}")
for i in range(total-1):
    smallest_index = i
    for j in range(i+1,total):
        if myselection[j]>myselection[smallest_index]:
            smallest_index = j
    minimum_value = myselection.pop(smallest_index)
    myselection.insert(i,minimum_value)
print(f"descending order = {myselection}")    