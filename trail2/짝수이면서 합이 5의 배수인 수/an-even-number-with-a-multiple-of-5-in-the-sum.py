n = int(input())

# Please write your code here.

def is_mn(n):
    # 2자리 숫자 
    # n이 짝수인지
    if n%2 == 0:
        # n의 각 자리 합이 5의 배수인지
        ten = n//10
        one = n%10

        if (ten+one) % 5 == 0:
            print("Yes")
            return
        else:
            print("No")
            return

    else:
        print("No")
        return

is_mn(n)






