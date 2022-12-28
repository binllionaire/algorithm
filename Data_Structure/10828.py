import sys
N = int(input())
stack = []
for _ in range(N):
    command = sys.stdin.readline()
    splitcommand = command.split()
    command = splitcommand[0]
    if(command == 'push'):
        x = splitcommand[1]
        stack.append(int(x))
    if(command == 'pop'):
        if(len(stack)>0):
            print(stack.pop())
        else:
            print(-1)
    if(command == 'size'):
        print(len(stack))
    if(command == 'empty'):
        if(len(stack) == 0): #스택이 비어있을 때
            print(1)
        else:
            print(0)
    if(command == 'top'):
        if(len(stack)>0):
            print(stack[-1])
        else:
            print(-1)

