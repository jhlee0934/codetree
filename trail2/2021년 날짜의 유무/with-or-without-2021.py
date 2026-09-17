M, D = map(int, input().split())

# Please write your code here.

# 날짜
# 1, 3, 5, 7, 8, 10, 12월은 31일까지
# 4, 6, 9, 11월은 30일 까지
# 2월은 28일 까지


def MD(M, D):
    if M in [1,3,5,7,8,10,12]:
        D_range = list(range(1,32))
        if D in D_range:
            print("Yes")
            return
    elif M in [4,6,9,11]:
        D_range = list(range(1,31))
        if D in D_range:
            print("Yes")
            return
    elif M == 2:
        D_range = list(range(1,29))
        if D in D_range:
            print("Yes")
            return
    
    print("No")

    return


MD(M,D)

        



