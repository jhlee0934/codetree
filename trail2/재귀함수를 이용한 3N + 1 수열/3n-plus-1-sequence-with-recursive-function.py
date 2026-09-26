n = int(input())

# Please write your code here.

count = 0

def f(n):
    global count

    if n == 1:
        return

    if n%2 == 0:
        count+= 1
        f(n//2)
        return
    else:
        count+=1
        f(n*3+1)
    
f(n)
print(count)