import random

def largest_fraction(arr):
    pair = merge_find(arr, [arr[0], arr[1]])
    print("aj = ", pair[1], "ai = ", pair[0], "aj/ai = ", pair[1]/pair[0])

def merge_find(arr, maxDiff):
    
    if len(arr) > 1:

        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]

        merge_find(left, maxDiff)
        merge_find(right, maxDiff)

        return merge(left, right, maxDiff)


def merge(left, right, maxDiff):

    i = j = 0

    lowest = left[0]
    highest = right[0]
    
    while i < len(left):
        if left[i] < lowest:
            lowest = left[i]
        i += 1

    while j < len(right):
        if right[j] > highest:
            highest = right[j]
        j += 1
        
    if highest - lowest > maxDiff[1] - maxDiff[0]:
        maxDiff[1] = highest
        maxDiff[0] = lowest
        
    return maxDiff
    

lst = [51,14,66,1,2,9,0,11]
print(largest_fraction(lst))

randArr = [random.randint(4, 700) for i in range(10)]
print("RANDARR : ", randArr)
print(largest_fraction(randArr))
