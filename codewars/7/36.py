def sum_digits(number):
    number=list(str(number))
    x=[]
    if number[0]=='-':
        del number[0]
    for i in number:
        x.append(int(i))
    return sum(x)