from collections import deque

def bfs(graph,x,y):

    # 상하좌우
    dx = [-1,1,0,0,-1,1,-1,1]
    dy = [0,0,-1,1,-1,1,1,-1]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0  #탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함

    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= b or ny <0 or ny >= a:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                
while(1):
    a,b = map(int,input().split())
    if(a==0 and b==0):
        break
    graph = [list(map(int, input().split())) for _ in range(b)]

    count = 0 
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1:
                bfs(graph,i,j)
                count += 1

    print(count)
