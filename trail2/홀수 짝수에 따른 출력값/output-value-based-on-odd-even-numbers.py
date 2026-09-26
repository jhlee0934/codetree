N = int(input())

# Please write your code here.

def f(N):
    # N이 홀수인 경우 1~N 까지의 홀수 합
    if N <= 2:
        return N

    
    return N + f(N-2)


print(f(N))
