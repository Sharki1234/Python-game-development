frequency = {}
#string
string = list("supercalafragelisticexpialodocious")
for i in range (len(string)):
    if string[i] not in frequency:
        frequency[string[i]] = 1
    else:
        frequency[string[i]]+=1

print(frequency)
