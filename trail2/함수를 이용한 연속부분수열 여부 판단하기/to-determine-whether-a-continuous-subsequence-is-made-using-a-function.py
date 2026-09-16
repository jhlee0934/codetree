n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.


def f(a,b,n1,n2):
    if n1 < n2 : 
        print("No")
        return

    # n2개 원소씩 슬라이싱

    for i in range(n1-n2+1):
        if a[i:i+n2] == b:
            print("Yes")
            return

    print("No")
f(a,b,n1,n2)



