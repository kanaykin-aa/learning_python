def printer_error(s):
    x=0
    for i in s:
        if i not in 'abcdefghijklm':
            x+=1
    return f'{x}/{len(s)}'