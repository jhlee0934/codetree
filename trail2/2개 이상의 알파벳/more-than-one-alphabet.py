A = input()

# Please write your code here.

def is_diff_char(A):
    n = len(A)
    for i in range(n):
        char = A[i]
        for j in range(i,n):
            if char != A[j]:
                print("Yes")
                return

    print("No")

is_diff_char(A)