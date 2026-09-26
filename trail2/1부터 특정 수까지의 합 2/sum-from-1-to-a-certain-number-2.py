N = int(input())

# Please write your code here.

def sum_n(N, result):
    if N == 0:
        return result

    result += N

    result = sum_n(N-1, result)

    return result

result = sum_n(N,0)
print(result)
