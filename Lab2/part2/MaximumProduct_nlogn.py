import sys
import random

def maxCross(arr, left, middle, right): 

    leftProd = rightProd = 1
    
    minSuffix = minPrefix = sys.maxsize

    maxPrefix = maxSuffix = -sys.maxsize
    
    for i in range(middle, left-1, -1):
        leftProd *= arr[i]
        minSuffix = min(leftProd, minSuffix)
        maxSuffix = max(leftProd, maxSuffix)
    
    for i in range(middle + 1, right + 1):
        rightProd *= arr[i]
        minPrefix = min(rightProd, minPrefix)
        maxPrefix = max(rightProd, maxPrefix)

    minToMin = minSuffix*minPrefix
    maxToMax = maxSuffix*maxPrefix
        
    maxCrossProd = max(minToMin, maxToMax)          

    return max(maxCrossProd, leftProd, rightProd)
  

def maxProduct(arr, left, right): 
      
    if left == right: 
        return arr[left] 

    middle = (left + right) // 2

    leftMax = maxProduct(arr, left, middle)
    rightMax = maxProduct(arr, middle+1, right)
    crossMax = maxCross(arr, left, middle, right)

    return max(leftMax, rightMax, crossMax)


arr1 = [-2, 3, -0.1, -40]
print(maxProduct(arr1, 0, len(arr1)-1))

arr2 = [-1, -2, -3, 4]
print(maxProduct(arr2, 0, len(arr2)-1))

arr3 = [-1, -3, -10, 0, 60]
print(maxProduct(arr3, 0, len(arr3)-1))

arr4 = [random.randint(-20,20) for i in range(4)]
print("RANDOM ARRAY: ", arr4)
print(maxProduct(arr4, 0, len(arr4)-1))
