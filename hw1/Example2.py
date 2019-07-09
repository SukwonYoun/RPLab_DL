#hw1 Ex2

def check_parentheses(input_expression):
    a=input_expression[0]

    n=0
    for i in a:
        if i=='(':
            n=n+1
        elif i==')':
            n=n-1
        else:
            continue
    m=0
    for j in a:
        if j=='{':
            m=m+1
        elif j=='}':
            m=m-1
        else:
            continue
    l=0
    for k in a:
        if k=='[':
            l=l+1
        elif i==']':
            l=l-1
        else:
            continue
    if n==0 and m==0 and l==0:
        result='Balanced'
    else:
        result='Unbalanced'

    return result
