def maxFrac(arr):
    print(arr)
    if len(arr)==2:
        return (arr[1]/arr[0], min(arr[0], arr[1]), max(arr[0], arr[1]))

    if len(arr)==3:
        maxFraction = max(arr[1]/arr[0], arr[2]/arr[1], arr[2]/arr[0])
        Min = min(arr[0], arr[1], arr[2])
        Max = max(arr[0], arr[1], arr[2])
        print(maxFraction)
        return (maxFraction, Min, Max)

    middle = len(arr)//2

    (leftFrac, leftMin, leftMax) = maxFrac(arr[0:middle])
    (rightFrac, rightMin, rightMax) = maxFrac(arr[middle:])

    maxFraction = max(leftFrac, rightFrac, rightMax/leftMin)
    
##    print(maxFraction)
##
##    print(arr)
    
    return (maxFraction, 1337, 1337)

lst = [70,7,4,2,55,5,7,8,4,5]
print(maxFrac(lst)[0])
