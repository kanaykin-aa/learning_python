def order(sentence):
    s=sentence.split()
    x=[]
    for i in range(1,len(s)+1):
        for k in s:
            if str(i) in k:
                x.append(k)
    return ' '.join(x)