Y, M, D = map(int, input().split())

# Please write your code here.


def is_yoon(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
               
        else:
            return True

    else:
        return False

def season(M):
    if M in [3,4,5]:
        return 'Spring'
    elif M in [6,7,8]:
        return 'Summer'
    elif M in [9,10,11]:
        return 'Fall'
    elif M in [12,1,2]:
        return 'Winter'


def is_YMD(Y,M,D):
    if M in [1,3,5,7,8,10,12]:
        D_range = list(range(32))
        if D in D_range:
            return season(M)
        else:
            return -1
    
    elif M in [4,6,9,11]:
        D_range = list(range(31))
        if D in D_range:
            return season(M)
        else:
            return -1
    elif M == 2:
        if is_yoon(Y):
            upper = 30
        else:
            upper = 29

        D_range = list(range(upper))
        if D in D_range:
            return season(M)
        else:
            return -1

    else:
        return -1

print(is_YMD(Y, M,D))