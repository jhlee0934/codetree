n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

# 인접 행렬
# adj = [[0]*(n+1) for _ in range(n+1)]

# for i, j in edges:
    
#     adj[i][j] = 1
#     adj[j][i] = 1

# visited = set({1})
# def dfs(i):
#     if sum(adj[i]) == 0:
#         return

    
#     for j in range(1,n+1):
#         if adj[i][j] != 1:
#             continue
#         if j in visited:
#             continue
            
#         visited.add(j)
#         dfs(j)


# dfs(1)
# print(len(visited)-1)

# 인접 리스트

adj = [[] for _ in range(n+1)]
for i, j in edges:
    adj[i].append(j)
    adj[j].append(i)

# print(adj)

visited = set({1})
def dfs(i):
    # 연결된 노드가 없으면 리턴
    if len(adj[i]) == 0:
        return

    visited.add(i)
    for j in adj[i]:
        if j in visited:
            continue
        dfs(j)

dfs(1)

print(len(visited)-1)




















