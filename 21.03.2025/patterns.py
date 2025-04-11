#pattern 1
board1 = []
for i in range(5):
  row1 = []
  for w in range(5):
    row1.append("*")
  board1.append(row1)

  print(''.join(board1[i]))

print("                                      ")
#pattern 2
board2 = []
for i in range(5):
  row2 = []
  row2.append("*"*(i+1))
  board2.append(row2)
  print(''.join(board2[i]))
print(" ")
#pattern3
board3 = []
for w in range(1,6):
  board3.append(str(w))
  print(''.join(board3))
print(" ")
#pattern4
board4 = []
x = 1

for i in range(5):
    row4 = []
    for m in range(x):
        row4.append(str(x))
        #print(row4)
    board4.append(row4)
    x+=1
    print(''.join(board4[i]))
print(" ")  
#pattern 5
board2 = []
for i in range(4,-1,-1):
  row2 = []
  row2.append("*"*(i+1))
  board2.append(row2)
  print(''.join(board2[4-i]))
print(" ")
#pattern6
board6 = []
x = 5

for i in range(5):
    row6 = []
    for m in range(x):
        row6.append(str(m+1))
        #print(row4)
    board6.append(row6)
    x-=1
    print(''.join(board6[i]))
print(" ")
#pattern7
board7 = []
row7 = []
f = []
k = ["*"]
g = []
w = -4

for m in range(4):
    f.append(" ")
    g.append(" ")
print(f"{''.join(f)}{''.join(k)}{''.join(g)}")
for x in range(3,-1,-1):
    f[x] = "*"
    g[w] = "*"
    w+=1
    print(f"{''.join(f)}{''.join(k)}{''.join(g)}")
print(" ")
#pattern 8
f = []
k = ["*"]
g = []
w = -4

for m in range(4):
    f.append("*")
    g.append("*")
print(f"{''.join(f)}{''.join(k)}{''.join(g)}")
for x in range(3,-1,-1):
    f[w] = " "
    g[x] = " "
    w+=1
    print(f"{''.join(f)}{''.join(k)}{''.join(g)}")


