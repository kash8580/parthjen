def palin(s):
    s=s.lower().replace(' ','')
    return s==s[::-1]

def rev(s):
    return s[::-1]