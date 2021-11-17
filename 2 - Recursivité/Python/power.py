def powerIt(b,n): #int b:base int n:exposant
    prod=1
    if n==0:return 1
    for i in range(n-1):
        prod=prod*b
        print(prod)
    return prod


def powerIt2(b,n):
    if n==0:return 1 #cas de base
    else:
        return b*powerIt2(b,n-1)

print(powerIt(2,5))
