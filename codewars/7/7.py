def longest(a1, a2):
    a3 = []
    a4 = a1 + a2
    if len(a1) >= len(a2):
        for i in a4:
            if i not in a3:
                a3.append(i)
    if len(a2) >= len(a1):
        for i in a4:
            if not i in a3:
                a3.append(i)
    return "".join(sorted(a3))
