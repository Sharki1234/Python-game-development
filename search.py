import random
search_list = random.sample(range(1,21),5)
print(search_list)
num = random.randint(1,20)
if num in search_list:
    print("Number found")
elif num not in search_list:
    print("Number not found")
print(f"Number:{num}")