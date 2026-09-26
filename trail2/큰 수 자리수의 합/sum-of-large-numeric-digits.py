a, b, c = map(int, input().split())

# Please write your code here.

abc = a* b * c

def f(n):
    if n < 10:
        return n

    result = n % 10

    return result + f(n//10)

print(f(abc))

