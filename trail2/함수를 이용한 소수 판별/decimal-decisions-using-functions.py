a, b = map(int, input().split())

# Please write your code here.

# 소수인지 확인하는 함수
# 소수란? 1 혹은 자기 자신으로만 나눠지는 수
# 즉, 2 부터 n-1 까지 나눠서 나머지가 0이 아니면 소수암

def is_sosu(n):


    for i in range(2,n):
        if n%i == 0:
            return False
    

    return True


sum = 0
for i in range(a, b+1):
    if is_sosu(i):
        sum += i


print(sum)










