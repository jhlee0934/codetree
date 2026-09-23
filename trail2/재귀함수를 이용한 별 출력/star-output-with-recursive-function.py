n = int(input())

# Please write your code here.

def star(a,n):
    if a > n:
        return

    result = '*'*a
    print(result)

    star(a+1,n)

star(1,n)


