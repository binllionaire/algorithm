import sys

size = int(input())
num = [0]*100001
for i in range(size):
    num[int(sys.stdin.readline())] += 1

for i in range(10001):
    if(num[i] != 0):
        for j in range(num[i]):
            print(i)
