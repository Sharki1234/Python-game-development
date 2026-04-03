import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(1,100)
num4 = random.randint(1,100)
num5 = random.randint(1,100)
myarray = [num1,num2,num3,num4,num5]
print(f"original array = {myarray}")
num = len(myarray)
for i in range(num-1):
    for j in range(num-i-1):
        if myarray[j]>myarray[j+1]:
            myarray[j],myarray[j+1]=myarray[j+1],myarray[j]
print(f"sorted ascending array = {myarray}")
for i in range(num-1):
    for j in range(num-i-1):
        if myarray[j]<myarray[j+1]:
            myarray[j],myarray[j+1]=myarray[j+1],myarray[j]
print(f"sorted descending array = {myarray}")