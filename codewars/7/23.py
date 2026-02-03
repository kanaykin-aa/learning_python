def capitals(word):
    x=[]
    for l, m in enumerate(word):
        if m==m.upper():
            x.append(l)
    return x