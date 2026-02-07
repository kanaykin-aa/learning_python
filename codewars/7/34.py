def number(lines):
    x=[]
    for i,j in enumerate(lines):
        x.append(f'{i+1}: {j}')
    return x