#palindromes
user = input("word?")
word = list(user)
reverse = []
for i in range(len(word)-1,0,-1):
  reverse.append(word[i])

if reverse == word:
  print("palindrome")
else:
  print("not palindrome")