a, b = map(int, input().split())

# Please write your code here.

# 소수인지
def f(n):
    for i in range(2,n):
        if n % i == 0:
            return False

    return True


# 모든 자리수 합이 짝수인지
def g(n):
    b = n // 100
    s = n // 10
    i = n % 10

    if (b + s+ i) % 2 == 0:
        return True
    else:
        return False


count = 0
for n in range(a,b+1):
    if f(n) and g(n):
        count += 1

print(count)



