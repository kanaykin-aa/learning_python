def queue_time(customers, n):
    kassa=[0]*n
    if customers==[]:
        return 0
    for i in customers:
        kassa_i=kassa.index(min(kassa))
        kassa[kassa_i]+=i
    return max(kassa)