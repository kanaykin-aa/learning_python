def number(bus_stops):
    v=[]
    w=[]
    for i in bus_stops:
        v.append(i[0])
        w.append(i[1])
    return sum(v)-sum(w)