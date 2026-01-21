def update_light(current):
    g='green'
    y='yellow'
    r='red'
    if current==g: return y
    elif current==y: return r
    else:
        return g