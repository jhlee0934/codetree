n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def absing(arr):
    for num in arr:
        print(abs(num), end = " ")


absing(arr)