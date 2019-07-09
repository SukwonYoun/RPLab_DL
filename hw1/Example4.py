#hw1 Ex4

def subsequences(a,n):
    b=list(a)
    l=[]
    for i in b:
        l.append(str(i))
        
    from itertools import combinations   
    c=list(combinations(l,n))

    m=[]
    for i in c:
        d=''.join(i)
        m.append(d)

    return tuple(m)
