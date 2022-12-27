N = int(input())
coordinate = []
for i in range(N):
    coordinate.append(list(map(int,input().split())))
coordinate.sort(key=lambda x:(x[1],x[0]))
for i in range(N):
    print(coordinate[i][0],coordinate[i][1])