def count_positives_sum_negatives(arr):
    if arr==[]:
        return []
    x=[]
    y=[]
    for i in arr:
        if i>0:
            x.append(i)
        else:
            y.append(i)

    return [len(x), sum(y)]