n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""

"""


def dig(x,y,k):
    x_lower = max(0,x-k)
    x_upper = min(n,x+k+1)
    y_lower = max(0,y-k)
    y_upper = min(n,y+k+1)

    count = 0

    for i in range(x_lower,x_upper):
        for j in range(y_lower,y_upper):
            if abs(x-i) + abs(y-j) <= k:
                count += grid[i][j]

    return count

result = 0
for i in range(n):
    for j in range(n):
        for k in range(2*n-1):
            cost = k**2 + (k+1)**2
            count = dig(i,j,k)
            benefit = m * count - cost
            if benefit >= 0:
                result = max(result, count)

                

print(result)

