import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)  

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(V):
    visited[V] = True  # 해당 V값 방문처리
    for i in graph[V]:
        if not visited[i]: # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            visited[i] = True
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)
       
count = 0
for i in range(1,N+1):
    if not visited[i]:
        count += 1
        dfs(i)
print(count)

