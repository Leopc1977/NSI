lst=[0 for i in range(100)]
lst[0]=1
lst[1]=1

def f(n):
    if lst[n]==0:
        lst
    if n<=1: return 1
    else : return f(n-2)+f(n-1)

print(f(4))
