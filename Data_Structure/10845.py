import sys
N = int(input())
queue = []
for _ in range(N):
    command = sys.stdin.readline()
    splitcommand = command.split()
    command = splitcommand[0]
    if(command == 'push'):
        x = splitcommand[1]
        queue.append(int(x))
    if(command == 'pop'):
        if(len(queue)>0):
            print(queue.pop(0))
        else:
            print(-1)
    if(command == 'size'):
        print(len(queue))
    if(command == 'empty'):
        if(len(queue) == 0): #스택이 비어있을 때
            print(1)
        else:
            print(0)
    if(command == 'front'):
        if(len(queue)>0):
            print(queue[0])
        else:
            print(-1)
    if(command == 'back'):
        if(len(queue)>0):
            print(queue[-1])
        else:
            print(-1)

