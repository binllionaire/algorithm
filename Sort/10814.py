N = int(input())
coordinate = []
for i in range(N):
    coordinate.append(list(map(str,input().split())))
coordinate.sort(key=lambda x:(int(x[0])))
for i in range(N):
    print(coordinate[i][0],coordinate[i][1])