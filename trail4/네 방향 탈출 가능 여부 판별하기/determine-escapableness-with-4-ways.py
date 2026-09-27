n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

"""
뱀이 없는 길은 1, 뱀이 있는 길은 0
dfs로 visited에 남아 있는 길은 패스
"""
from collections import deque
# 상, 우, 하, 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 방문한 길을 저장하는 2차원 배열
visited = [[0]*m for _ in range(n)]

# 현재 위치의 상하좌우를 스캔하는 함수
# 그리드 범위를 벗어나거나, 이미 방문한 좌표거나 뱀이 있으면 제외한다.
def scan(x,y):
    next = []
    for dir in range(4):
        if x+dx[dir] < 0 or x+dx[dir] > n-1:
            continue

        if y+dy[dir] < 0 or y+dy[dir] > m-1:
            continue

        if grid[x+dx[dir]][y+dy[dir]] == 0:
            continue

        if visited[x+dx[dir]][y+dy[dir]] == 1:
            continue
            
        next.append((x+dx[dir],y+dy[dir]))

    return next

def dfs(x,y):
    global exit
    if (x,y) == (n-1,m-1):
        # print(visited)
        exit = True
        return

    next = scan(x,y)

    for i, j in next:
        visited[i][j] = 1
        dfs(i,j)
        visited[i][j] = 0

def bfs(x,y):
    q = deque(scan(x,y))
    while q:
        x, y = q.popleft()

        next = scan(x,y)
        for nx, ny in next:
            visited[nx][ny] = 1
            q.append((nx,ny))
        
        
        
bfs(0,0)
print(visited[n-1][m-1])







