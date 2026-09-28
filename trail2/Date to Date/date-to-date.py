m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

def days(m1, d1, m2, d2):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    prefix = [0]

    for i in range(12):
        new_value = prefix[i]+months[i]
        prefix.append(new_value)

    return prefix[m2-1] - prefix[m1-1] + d2 - d1 +1



print(days(m1, d1, m2, d2))
    
