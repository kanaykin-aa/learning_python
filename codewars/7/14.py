def get_count(sentence):
    x=[]
    for i in sentence:
        if i in 'aeiou':
            x.append(i)
    return len(x)