#hw1 Ex5

def sort_tuple(input_dict):
    a=input_dict.items()
    b=list(a)
    c={}
    for (first,last) in b:
        c[last]=first

    d=sorted(c.items())

    e=[]
    for (first,last) in d:
        e.append(last)

    return tuple(e)
