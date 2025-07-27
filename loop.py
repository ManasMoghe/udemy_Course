n=8
def fibo(n):
    if n==0:
        return(0)
    elif n==1:
        return(1)
    else:
        a=0
        b=1
        m=[a,b]
        for i in range(n-2):
            s=a+b
            a=b
            b=s
            m.append(s)
        return(m)
fibonacci=fibo(n)
print(fibonacci)
