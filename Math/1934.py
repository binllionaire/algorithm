import sys
T = int(input())
for _ in range(T):
    A,B = map(int,sys.stdin.readline().split())
    lcm = A * B
    while (A!=0):
        B=B%A
        A,B = B,A
    gcd = B
    lcm = lcm // B
    print(lcm)