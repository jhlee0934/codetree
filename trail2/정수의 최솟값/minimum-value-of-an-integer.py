a, b, c = map(int, input().split())

# Please write your code here.


def find_min(a,b,c):

    if b < a:
        if b < c:
            return b
        else:
            return c
    elif c < a: # a <= b
        return c
    else:
        return a
    

result = find_min(a,b,c)

print(result)




