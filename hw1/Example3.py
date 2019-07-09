#hw1 Ex3

def check(str1, str2):
    a=",".join(str1)
    b=a.split(',')
    b.sort()
    c=",".join(str2)
    d=c.split(',')
    d.sort()
    if b==d:
        result='True'
    else:
        result='False'
    return result
    
