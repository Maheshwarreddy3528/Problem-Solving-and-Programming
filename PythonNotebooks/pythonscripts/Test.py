def fact(n):
    if n == 1:
        return n
    else:
        return (n*fact(n-1))
    
    
def sums(n):
    if n==1:
        return 1
    else:
        return n+sums(n-1)