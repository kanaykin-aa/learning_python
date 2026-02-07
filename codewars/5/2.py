import string
def rot13(message):
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    answ=''
    for i in message:
        if i in lower:
            new=(lower.index(i)+13)%26
            answ+=lower[new]
        elif i in upper:
            new=(upper.index(i)+13)%26
            answ+=upper[new]
        else:
            answ+=i
    return answ