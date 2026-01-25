def sort_array(source_array):
    x=[]
    z=[]
    for i in source_array:
        if i%2!=0:
            x.append(i)
    xx=sorted(x)
    for i in source_array:
            if i%2!=0:
                z.append(xx[0])
                xx.pop(0)
            else:
                z.append(i)
    return z