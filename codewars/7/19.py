def remove_smallest(numbers):
    if numbers==[]:
        return []
    x=numbers.copy()
    y=min(x)
    x.remove(y)
    return x