def bouncing_ball(h, bounce, window):
    if h<0:
        return -1
    elif not 0<bounce<1:
        return -1
    elif window==h:
        return -1
    x=1
    h*=bounce
    while h>window:
        x+=2
        h*=bounce
    return x