n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

"""
블럭1과 블럭2로 클래스를 나누어 고려
모든 시작 위치(x,y)를 순회하며 각 방향 마다 합을 계산하게 한 뒤,
맥시멈을 비교

"""

class Block1:
    def __init__(self,x,y,dir):
        
        self.x = x
        self.y = y
        self.dir = dir

    def block_sum(self):
        x = self.x
        y = self.y
        if dir == 0: # 니은
            return grid[x][y] + grid[x+1][y] + grid[x+1][y+1]
        elif dir == 1: # 기역
            return grid[x][y] + grid[x][y+1] + grid[x+1][y+1]
        elif dir == 2: # 뒤집한 기역
            return grid[x][y] + grid[x+1][y] + grid[x][y+1]
        elif dir == 3:
            return grid[x+1][y] + grid[x][y+1] + grid[x+1][y+1]

class Block2:
    def __init__(self,x,y,dir):
        self.x = x
        self.y = y
        self.dir = dir

    def block_sum(self):
        x = self.x
        y = self.y

        if dir == 0: # 가로
            return grid[x][y] + grid[x][y+1] + grid[x][y+2]
        elif dir == 1: 
            return grid[x][y] + grid[x+1][y] + grid[x+2][y]


# 블럭1 순회
# 블럭 1은 n-1, m-1까지만 순회하면 됨
maximum = 0

for i in range(n-1):
    for j in range(m-1):
        for dir in range(4):
            block = Block1(i,j,dir)
            maximum = max(maximum, block.block_sum())


# 블럭2 순회
# 모든 좌표를 순회하되, 각 dir 별로 각이 안나오면 컨티뉴

for i in range(n):
    for j in range(m):
        for dir in range(2):
            if dir == 0 and j + 3 > m:
                continue
            elif dir == 1 and i + 3 > n:
                continue
            block = Block2(i,j,dir)
            maximum = max(maximum, block.block_sum())

print(maximum)


