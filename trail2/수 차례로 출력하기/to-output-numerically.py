n = int(input())

# Please write your code here.
N = n

def print_num(n):
    global N
    if n == 0:
        return

    print(N-n+1, end = " ")
    print_num(n-1)

def print_num_inv(n):
    if n == 0:
        return

    print(n, end = " ")
    print_num_inv(n-1)


print_num(n)
print("")
print_num_inv(n)


