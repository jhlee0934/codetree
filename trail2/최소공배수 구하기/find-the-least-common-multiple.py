n, m = map(int, input().split())

# Please write your code here.

def gcm(a,b):
    n = max(a,b)
    m = min(a,b)

    for i in range(1,m+1): # 아무리 못해도 m*n은 최소 공배수가 됨
        gcm = n * i
        if gcm % m ==0:
            return gcm
    

a = gcm(n,m)
print(a)
