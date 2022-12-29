import sys

s1 = list(input())
s2 = []

for _ in range(int(input())):
    command = str(sys.stdin.readline())
    command_arg = command.split()
    command = command[0]
    if(command == 'P'):
        s1.append(command_arg[1])
    if(command == 'L' and s1): #s1에 값이 있을 때
        s2.append(s1.pop()) #s1의 마지막 값을 s2의 마지막에 append
    if(command == 'D' and s2):
        s1.append(s2.pop())
    if(command == 'B' and s1):
        s1.pop()
s1.extend(reversed(s2))
print(''.join(s1))
