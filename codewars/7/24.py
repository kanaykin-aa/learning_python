def calculate_years(principal, interest, tax, desired):
    year=(principal*interest)-(principal*interest)*tax
    ans=0
    while principal<desired:
        principal=principal+((principal*interest)-(principal*interest)*tax)
        ans+=1
    return ans