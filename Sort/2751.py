import sys

size = int(input())
num = [0]*size
for i in range(size):
    num[i] = int(sys.stdin.readline())
num.sort()
for i in range(size):
    print(num[i])


