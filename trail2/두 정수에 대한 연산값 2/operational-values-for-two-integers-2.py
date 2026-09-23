a, b = map(int, input().split())

# Please write your code here.

def f(a, b):
    if a > b:
        print(a * 2, b + 10)
    else:
        print(a + 10, b * 2)


f(a, b)