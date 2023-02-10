import sys
from collections import deque
sys.setrecursionlimit(11111111)

def bfs(graph,ilist,jlist,count):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    newilist = []
    newjlist = []
    while ilist:
        x = ilist.pop()
        y = jlist.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= b or ny <0 or ny >= a:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                newilist.append(nx)
                newjlist.append(ny)
            
    if len(newilist)>0: 
        count += 1 
        bfs(graph,newilist,newjlist,count)
    else:
        if not isAllRiped():
            count = -1
            print(count)
        else:
            print(count)


def isAllRiped():
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 0:
                return False
    return True   
    
a,b = map(int,input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(b)]

count = 0 
ilist = []
jlist = []

for i in range(b):
    for j in range(a):
        if graph[i][j] == 1:
            ilist.append(i)
            jlist.append(j)
bfs(graph,ilist,jlist,count)


