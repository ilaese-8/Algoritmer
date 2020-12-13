import random

def maxProduct(arr):
    
    if len(arr) == 1:
        print(arr)
        return
    
    sub = split(arr, [arr[0]])
    print(sub)

def split(arr, sub):
    
    if len(arr) > 1:

        middle = len(arr)//2
        L = arr[:middle]
        R = arr[middle:]

        split(L, sub)
        split(R, sub)

        return maxSub(L, R, sub)


def maxSub(L, R, sub):

    print(L)
    print(R)
    
    i = j = 1

    lProd = L[0]
    rProd = R[0]
    
    while i < len(L):
        lProd *= L[i]
        i += 1

    while j < len(R):
        rProd *= R[j]
        j += 1
        
    maxProd = 1
    for element in sub:
        maxProd *= element

    if lProd*rProd > maxProd:
        
        del sub[:]
        for i in L:
            sub.append(i)
        for j in R:
            sub.append(j)
            

    if lProd > rProd and lProd > maxProd and lProd*rProd < maxProd:
        del sub[:]
        for i in L:
            sub.append(i)

    if rProd > lProd and rProd > maxProd and lProd*rProd < maxProd:
        del sub[:]
        for i in R:
            sub.append(i)

    return sub
    

lst = [-2, 3, -2, -40]
maxProduct(lst)

randArr = [random.randint(-50, 50) for i in range(8)]
print("RANDARR : ", randArr)
maxProduct(randArr)
