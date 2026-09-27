n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.




def happy():
    count = 0
    # 가로
    for i in range(n):
        for j in range(n-m+1):
            happy = True # m개 검사 스타팅 포인트
            for k in range(1,m):
                if grid[i][j+k-1] == grid[i][j+k]:
                    continue
                else:
                    happy = False
            if happy:
                count += 1
                break
    # 세로
    for j in range(n):
        for i in range(n-m+1):
            happy = True # m개 검사 스타팅 포인트
            for k in range(1,m):
                if grid[i+k-1][j] == grid[i+k][j]:
                    continue
                else:
                    happy = False
            if happy:
                count += 1
                break


    return count

print(happy())