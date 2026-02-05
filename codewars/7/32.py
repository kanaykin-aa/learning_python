def stray(arr):
    x=[]
    for i in arr:
        if arr.count(i)==1:
            x.append(i)
    return sum(x)