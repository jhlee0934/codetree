N = int(input())

# Please write your code here.

def print_n(a,n):
    if a > 2*n:
        return
    if n-a != 0:
        print(abs(n-a), end = " ")
    print_n(a+1,n)


print_n(0,N)
