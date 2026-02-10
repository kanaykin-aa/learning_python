def reverse_letter(st):
    x=[]
    for i in st:
        if i.isalpha():
            x.append(i)
    x.reverse()
    return "".join(x)