def solve(s):
    x=0
    y=0
    for i in s:
        if i.isupper():
            x+=1
        else:
            y+=1
    if x>y:
        return s.upper()
    else:
        return s.lower()