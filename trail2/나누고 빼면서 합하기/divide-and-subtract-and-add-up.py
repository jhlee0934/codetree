n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def f(m):
    result = A[m-1]

    while m != 1:
        if m % 2 == 0:
            m = m // 2
        else:
            m -= 1
        result += A[m-1]
    return result

if m == 1:
    print(A[m-1])
else:
    
    result = f(m)
    print(result)




