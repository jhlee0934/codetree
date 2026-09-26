n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


def max_(n,arr):
    if n == 0:
        return arr[0]

    mmm= arr[n-1]
    return max(max_(n-1,arr), mmm)

print(max_(n,arr))