n, m = map(int, input().split())

# Please write your code here.
def gcd(a,b):
    n = max(a,b)
    m = min(a,b)
    gcd = -1
    for i in range(1,m+1):
        if m % i == 0 and n % i == 0:
            gcd = i

    return gcd

a = gcd(n,m)
print(a)
