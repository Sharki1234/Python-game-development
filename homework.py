import random
Number = random.randint(1,21)
Question = int(input("Please guess the number"))
if Question < Number:
    print("too low")
elif Question > Number:
    print("too high")
elif Question == Number:
    print("Correct!You guessed the number")