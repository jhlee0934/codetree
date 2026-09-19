a, b = map(int, input().split())

# Please write your code here.

def f(a, b):
    if a >= b:
        a_ = a+25
        b_ = b*2
    else:
        a_ = a*2
        b_ = b+25

    return a_, b_

print(*f(a,b))
