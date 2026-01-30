def tower_builder(n_floors):
    x=[]
    y='*'
    for i in range(n_floors):
        x.append(((y*i+y)+y*i).center((n_floors * 2 - 1), " "))
    return x