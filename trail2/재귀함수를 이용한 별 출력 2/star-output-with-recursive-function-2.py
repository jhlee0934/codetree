n = int(input())

# Please write your code here.

def print_star(a,n):
    if a > 2*n:
        return

    if a != n:
        star = '* '*abs(n-a)
        print(star)

    print_star(a+1,n)


print_star(0,n)
