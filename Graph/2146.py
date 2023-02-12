from collections import deque
import sys
sys.setrecursionlimit(111111)

def continent_division(graph,x,y,label):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = label

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = label
                queue.append((nx,ny))
               

def bridge(label):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    distance = [[0]* N for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == label:
                queue.append([i, j])
    
    while queue:
        global answer
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue
            # 바다를 만났을 때
            if graph[nx][ny] == 0 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))
            # 땅을 만났을 때
            if graph[nx][ny] > 0 and graph[nx][ny] != label:
                answer = min(answer,distance[x][y])
                return   


N = int(input())
# 대륙분류하기
graph = [list(map(int, input().split())) for _ in range(N)]

label = 1
answer = sys.maxsize
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            label += 1
            continent_division(graph, i, j, label)
            
# 다리놓기
for i in range(2,label):
    bridge(i)

print(answer)