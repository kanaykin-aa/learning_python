def high_and_low(numbers):
    x=[]
    numbers=numbers.split()
    for i in numbers:
        x.append(int(i))
    return f"{max(x)} {min(x)}"