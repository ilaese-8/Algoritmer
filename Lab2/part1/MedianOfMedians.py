import random
import sys

def select(arr):

    chunks = [arr[i : i+5] for i in range(0, len(arr), 5)]
    print(chunks)
    sorted_chunks = [sorted(chunk) for chunk in chunks]
    medians = [chunk[len(chunk) // 2] for chunk in sorted_chunks]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = select(medians)

    p = partition(arr, pivot)

    if p == 2:
        return sorted(arr[0:2 + 1])
    if p > 2:
        return select(arr[0:p])
    else:
        return select(arr[p+1:len(arr)])


def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == pivot: 
            i += 1
        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return left


randArr = [1]
for i in range(0, 100):
    randArr.append(random.randint(4, 700))                 
print("RANDARR : ", randArr)
print(select(randArr))

#arr = [9, 3, 177, 88, 4, 7, 25]
#print(select(arr))
