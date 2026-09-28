a, b, c, d = map(int, input().split())

# Please write your code here.

def timer(a, b, c, d):
    from_ = a*60 + b
    to_ = c*60 + d

    return to_ - from_
    


    

print(timer(a,b,c,d))