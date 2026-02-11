def gimme(input_array):
    for i in input_array:
        if i!=min(input_array) and i!=max(input_array):
            return input_array.index(i)