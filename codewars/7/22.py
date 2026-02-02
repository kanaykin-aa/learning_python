def reverse_words(text):
    x=text.split(' ')
    y=[]
    for i in x:
        y.append(i[::-1])
    return " ".join(y)