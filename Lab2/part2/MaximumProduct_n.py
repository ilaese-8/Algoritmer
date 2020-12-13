def maxProduct(arr):
    
    if len(arr) == 1:
        return arr

    return [arr[0]] + maxProduct(arr[1:])

lst = [2, 3, 2, 40]
print(maxProduct(lst))
