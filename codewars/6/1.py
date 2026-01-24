def is_pangram(st):
    st=st.lower()
    a='abcdefghijklmnopqrstuvwxyz'
    for i in a:
        if i not in st:
            return False
    return True