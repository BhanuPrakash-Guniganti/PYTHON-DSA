li = ["--X","X++","X++","X--"]
x = 4
for i in range(len(li)):
  temp = li[i]
  if temp == "--X":
    x = x - 1
  if temp == "X++":
    x = x + 1
  if temp == "X++":
    x = x + 1
  if temp == "X--":
    x = x - 1
print(x)
    

