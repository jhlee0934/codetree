N = int(input())

# Please write your code here.

count = 0
def f(N):
    global count

    if N == 1:
        return 

    if N % 2 == 0:
        count += 1
        f(N//2)
        return 
    else:
        count += 1
        f(N//3)
        return 

f(N)

print(count)