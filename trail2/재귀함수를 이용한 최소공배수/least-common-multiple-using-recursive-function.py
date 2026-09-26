n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

"""
두 수 A, B의 최소공배수는 A*B / (A*B의 최대공약수)
즉, 재귀적으로 최대공약수를 만들면 됨

유클리드 호제법에 의해 최대공약수를 구하는 법
a> b라고 할 때 
a, b의 최대공약수는 a = b * q + r이면, b와 r의 최대공약수와 같다.
또한 r= 0이면, a,b의 최대공약수는 b가 된다.

"""


# 최대공약수
def gcd(a,b):
    max_ = max(a,b)
    min_ = min(a,b)

    if max_ % min_ == 0:
        return min_

    return gcd(min_, max_%min_)


"""
두 수 A, B의 최소공배수는 A*B / (A*B의 최대공약수)
즉, 재귀적으로 최대공약수를 만들면 됨
"""
# 최소공배수
# a는 초기값, b는 arr의 인덱스
def lcm(a,b):
    
    return (a * b) // gcd(a , b)

def f(i):
    if i == n-1:
        return arr[i]
    
    return lcm(f(i + 1), arr[i])

print(f(0))



    
