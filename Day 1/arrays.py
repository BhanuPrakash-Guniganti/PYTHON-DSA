"""

a1 = 10
a2 = 9
a3 = 8
a4 = 7
print(a1)
print(a2)
print(a3)
print(a4)


Instead of writing each variable separately, we can use an array to store the values and print them. Here's an example:

"""
"""

a = [10, 9, 8, 7, "Bhanu"]

print (a[0])
print (a[1])
print (a[2])
print (a[3])
print (a[4])

"""

"""
a = [10, 9, 8, 7, "Bhanu"]
for i in range(2):
    print (a[i])

"""


"""

#now lets see insertion, deletion, updation any its types in arrays


#Insertion (.append & .insert) 
arr = [10, 20, 30, 40]
arr.append(50)   #Adds at the end of an array
print(arr)


"""

arr = [10,20,30]
arr.insert(1, 50)  #(index, value)
print(arr)


"""

#Updating (using index value)
arr = [10, 20, 30, 40]
arr [2] = 50
print(arr)

"""

#Removal (pop, remove, delete)



"""
# (.pop) Removes the last element from index

arr = [10, 20, 30, 40, 50, 60]
arr.pop()
print(arr)

"""

"""

arr = [10, 20, 30, 40, 20, 60]
arr.remove(20)   #removes the first occurance of the number 20
print(arr)

"""


"""

arr = [10, 20, 30, 40, 50, 60]
del arr[4]                     #Deletes the index 4
print(arr)

"""




