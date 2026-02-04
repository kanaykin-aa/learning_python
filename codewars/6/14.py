def duplicate_encode(word):
    word=word.lower()
    x=[]
    for i in word:
        if word.count(i)==1:
            x.append('(')
        else:
            x.append(')')
    return "".join(x)