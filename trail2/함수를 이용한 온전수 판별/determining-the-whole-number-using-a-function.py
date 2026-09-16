a, b = map(int, input().split())

# Please write your code here.


def onj(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif n % 3 == 0 and n % 9 !=0:
        return False
    else:
        return True


count = 0
for n in range(a,b+1):
    if onj(n):
        count += 1


print(count)


