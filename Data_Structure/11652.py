import sys
N = int(input())
dic = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
dic = dict(sorted(dic.items())) # key값 오름차순 정렬
print(max(dic,key=dic.get)) #value중 최대값의 key값 가져오기
