def duplicate_count(text):
    text=text.lower()
    t=0
    for i in set(text):
        if text.count(i)>=2:
            t+=1
    return t