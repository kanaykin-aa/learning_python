def domain_name(url):
    a=url.replace("http://", '').replace("https://", '').replace("https://", '').replace("www.", '')
    x=a.split('.')
    return x[0]