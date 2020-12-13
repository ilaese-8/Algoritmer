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
        return sub


    elif lProd*R[0] > maxProd:
        del sub[:]
        for i in L:
            sub.append(i)
        sub.append(R[0])
        return sub


    elif rProd*L[len(L)-1] > maxProd:
        del sub[:]
        sub.append(L[len(L)-1])
        for i in R:
            sub.append(i)
        return sub
            

    if lProd >= rProd and lProd >= maxProd and lProd*rProd <= maxProd:
        del sub[:]
        for i in L:
            sub.append(i)
        if R[0] > 0:
            sub.append(R[0])

    if rProd >= lProd and rProd >= maxProd and lProd*rProd <= maxProd:
        del sub[:]
        if L[len(L)-1] > 0:
            sub.append(L[len(L)-1])
        for i in R:
            sub.append(i)
        

    return sub
    

lst1 = [6, -3, -10, 0]
lst2 = [-2, -3, 0, -2, -40]
lst3 = [-1, -3, -10, 0, 60]
lst4 = [-1, -2, -3, 4]
maxProduct(lst1)
maxProduct(lst2)
maxProduct(lst3)
maxProduct(lst4)
