n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def get_sum(a, b):
    global arr

    result = arr[a-1: b]
    return sum(result)


for a, b in queries:
    print(get_sum(a, b))
