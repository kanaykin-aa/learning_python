def friend(x):
    y=[]
    for i in x:
        if i==i[:4] and i!=i[:3] and i!=i[:2] and i!=i[:1]:
            y.append(i)
    return y