import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n+1)]


for i in range(m):
    p, q, d = edges[i] # p노드에서 q노드까지 거리 d
    graph[p].append((d,q)) # 힙 정렬을 위해 거리를 먼저 넣음 ***

# print(graph)

INF = float('inf')


def dijkstra(start):
    # 거리 초기값은 모두 무한대
    distance = [INF]*(n+1)
    # 자기 자신과의 거리는 0
    distance[start] = 0

    pq = []
    # 힙을 사용해서 자동으로 거리가 가장 짧은 지점이 다음에 튀어나오는게 포인트
    heapq.heappush(pq, (0,start))

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist: # 현재 저장된 경로가 더 짧으면, 스킵
            continue

        for cost, next_node in graph[now]:
            new_dist = dist+cost

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq,(new_dist, next_node))

    return distance

dist = dijkstra(1)
for i in range(2,n+1): # 0번은 패딩, 1번은 자기 자신이므로 2번부터 출력
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])

    
    
