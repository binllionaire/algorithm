import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v,start):
    if not visited[num[v-1]]:
        visited[num[v-1]]=True
        if(num[v-1]!=start):
            dfs(num[v-1],start)
for _ in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)  
    for i in range(len(num)):
        graph[i+1].append(num[i])
    print(graph)
    count = 0
    for i in range(1,N+1):
        if not visited[i]:
            count += 1
            dfs(i,i)
    print(count)