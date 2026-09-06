n = int(input())

# Please write your code here.
def one_square(n):
    count = 0
    for i in range(n):
        if i != 0:
            print("")
        for j in range(n):
            count +=1
            if count >= 10:
                count = 1
            print(count, end = " ")

one_square(n)