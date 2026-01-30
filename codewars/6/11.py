def wave(people):
    x=[]
    for i in range(len(people)):
        if people[i]!=" ":
            x.append(people[:i]+people[i].upper()+people[i+1:])
    return x