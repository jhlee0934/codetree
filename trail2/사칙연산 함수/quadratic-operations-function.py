a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.


def f(a,o,b):
    if o == '+':
        print(f"{a} {o} {c} = {a+b}")

    elif o == '-':
        print(f"{a} {o} {c} = {a-b}")

    elif o == '*':
        print(f"{a} {o} {c} = {a*b}")

    elif o == '/':
        print(f"{a} {o} {c} = {a//b}")

    else:
        print(False)

f(a,o,c)







