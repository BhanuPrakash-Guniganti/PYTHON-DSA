arr = [3, 5, 0, 0, 4]

count = 0 #count starts from 0

for i in range(len(arr)):
    if arr[i] != 0: #not eqaul to 0
        arr[i], arr[count] = arr[count], arr[i]
        count += 1

print(arr)