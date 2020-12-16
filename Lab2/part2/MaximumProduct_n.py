def maxProduct(arr):
    return maxProd(arr, 1, 0)

# rp = running product, mp = max product, nrp = new running product
def maxProd(arr, rp, mp):

    if len(arr) == 0:
        return mp
    
    nrp = rp * arr[0]
    mp = max(mp, nrp)
    
    if nrp < 1:
        return maxProd(arr[1:], 1, mp)
    return maxProd(arr[1:], nrp, mp)


lst = [2, 3, 0.9, 40]
print(maxProduct(lst))
