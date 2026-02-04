def series_sum(n):
    x=[1,]
    for i in range(4,10000,3):
        x.append(1/i)
    return f'{sum(x[:n]):.2f}'