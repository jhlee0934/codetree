n = int(input())

# Please write your code here.

def call(n):
    if n == 0:
        return
    print("HelloWorld")
    call(n-1)

call(n)