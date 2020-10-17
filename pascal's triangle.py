# this code prints pascal's triangle to a certain number of rows (as requested by the user)
n = int(input("Number of rows: "))
row = 2
prevlist = [1, 1]
print(1)
print(1, 1)
for i in range(n-2):
  row += 1
  newlist = []
  for j in range(row):
    if j == 0 or j == len(prevlist):
      newlist.append(1)
    else:
      newlist.append(prevlist[j-1] + prevlist[j])
  for k in range(len(newlist)-1):
    print(newlist[k], end=" ")
  print(newlist[-1])
  prevlist = newlist
