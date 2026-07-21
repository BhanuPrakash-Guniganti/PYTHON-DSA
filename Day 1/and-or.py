"""

if ((2 + 1 == 3) and (5 + 1 == 7)):
    print("Answer is correct")
else:
    ("Incorrect")    

"""

li = [3, 6, 9, 10, 15, 8, 7]
ans = 0
for i in li:
    if ((i%2 == 0) or (i%3 == 0)): #you can use anyone AND or OR
        ans = ans + 1
        print(ans)