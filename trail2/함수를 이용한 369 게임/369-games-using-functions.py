a, b = map(int, input().split())

# Please write your code here.

# 숫자가 3 6 9 를 포함하는지 체크하는 함수
def check369(n):
    n = str(n)

    for num in n:
        if int(num) == 3 or int(num) == 6 or int(num) == 9:
            return True
    
    return False

def check3mul(n):
    if n%3 == 0:
        return True
    
    else:
        return False

def check_369_3(a,b):
    count = 0
    for n in range(a, b+1):
        if check3mul(n) or check369(n):
            count +=1

    return count


count = check_369_3(a, b)

print(count)




