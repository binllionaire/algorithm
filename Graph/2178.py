from collections import deque

def bfs(graph,x,y):

    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= b or ny <0 or ny >= a:
                continue
            
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

b,a = map(int,input().split())
graph = [list(map(int, input())) for _ in range(b)]

bfs(graph,0,0)
print(graph[b-1][a-1])
