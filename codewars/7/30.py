def to_jaden_case(string):
    string=string.split()
    x=[]
    for i in string:
        x.append(i[0].upper()+i[1:].lower())
    return " ".join(x)