import sys
import random

def maxCross(arr, left, middle, right): 

    leftProd = rightProd = 1
    
    minSuffix = minPrefix = sys.maxsize

    maxPrefix = maxSuffix = -sys.maxsize
    
    minSuffixIndex = maxSuffixIndex = middle
    
    minPrefixIndex = maxPrefixIndex = middle + 1
    
    for i in range(middle, left-1, -1):
        
        leftProd *= arr[i]
        
        if leftProd < minSuffix:
            minSuffix = leftProd
            minSuffixIndex = i
            
        if leftProd > maxSuffix:
            maxSuffix = leftProd
            maxSuffixIndex = i
    
    for i in range(middle + 1, right + 1):
        rightProd *= arr[i]

        if rightProd < minPrefix:
            minPrefix = rightProd
            minPrefixIndex = i

        if rightProd > maxPrefix:
            maxPrefix = rightProd
            maxPrefixIndex = i

    
    minToMin = 1
    for i in range(middle + 1, minPrefixIndex + 1):
        minToMin *= arr[i]
        
    for i in range(middle, minSuffixIndex-1, -1):
        minToMin *= arr[i]

    maxToMax = 1
    for i in range(middle + 1, maxPrefixIndex + 1):
        maxToMax *= arr[i]
        
    for i in range(middle, maxSuffixIndex-1, -1):
        maxToMax *= arr[i]

    maxCrossProd = max(minToMin, maxToMax)          

    fullProd = leftProd * rightProd

    return max(maxCrossProd, fullProd, leftProd, rightProd)
  

def maxProduct(arr, left, right): 
      
    if left == right: 
        return arr[left] 

    middle = (left + right) // 2

    leftMax = maxProduct(arr, left, middle)
    rightMax = maxProduct(arr, middle+1, right)
    crossMax = maxCross(arr, left, middle, right)

    return max(leftMax, rightMax, crossMax)


arr1 = [-2, 3, -2, -40]
print(maxProduct(arr1, 0, len(arr1)-1))

arr2 = [-1, -2, -3, 4]
print(maxProduct(arr2, 0, len(arr2)-1))

arr3 = [-1, -3, -10, 0, 60]
print(maxProduct(arr3, 0, len(arr3)-1))

arr4 = [random.randint(-20,20) for i in range(4)]
print("RANDOM ARRAY: ", arr4)
print(maxProduct(arr4, 0, len(arr4)-1))
