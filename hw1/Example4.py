#hw1 Ex4

def subsequences(a,n):
    from itertools import combinations
    b=list(a)
    c=list(combinations(b,n))

    m=[]
    for i in c:
        d=''.join(i)
        m.append(d)

    return tuple(m)
