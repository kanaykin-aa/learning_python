def find_average(numbers):
    if numbers==[]:
        numbers=sum(numbers)
    else:
        numbers=sum(numbers)/len(numbers)
    return(numbers)