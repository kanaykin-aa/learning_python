def past(h, m, s):
    h=h*3600000
    m=m*60000
    s=s*1000
    if h==0:
        x=m+s
    elif m==0:
        x=h+s
    else:
        x=h+m+s
    return x