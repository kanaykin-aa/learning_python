def descending_order(num):
    x=[]
    for i in str(num):
        x.append(i)
    x.sort(reverse=True)
    return int("".join(x))