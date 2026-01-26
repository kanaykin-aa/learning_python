def sum_array(arr):
    if arr==None:
        return 0
    else:
        arr=sorted(arr)
        return sum(arr[1:len(arr)-1])
