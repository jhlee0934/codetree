N = int(input())

# Please write your code here.

def each_pos_sq(N):

    if N < 10:
        return N**2

    pos = N % 10
    pos = pos**2

    result = each_pos_sq(N // 10)

    return pos + result


result = each_pos_sq(N)
print(result)

