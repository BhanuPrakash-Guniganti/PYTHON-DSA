arr = [10, 20, 5, 6, 30, 22, 32]

n = len(arr) #finding length of arr

if n < 2: #mean if less than 2 mean the single number, so we cant find second largest then the answer will be -1
    print(-1)
else:
    first = second = float('-inf') #

    for num in arr: #numbers in array
        if num > first: # if the number is greater than -inf
            second = first #stores in first
            first = num #if the num is greter than the second moves to first

        elif num > second and num != first:
            second = num 

    if second == float('-inf'):
        print(-1)
    else:
        print(second)