import sys
N = int(input())
deque = []
for _ in range(N):
    command = sys.stdin.readline()
    splitcommand = command.split()
    command = splitcommand[0]
    if(command == 'push_front'):
        x = splitcommand[1]
        deque.insert(0,int(x))
    if(command == 'push_back'):
        x = splitcommand[1]
        deque.append(int(x))
    if(command == 'pop_front'):
        if(len(deque)>0):
            print(deque.pop(0))
        else:
            print(-1)
    if(command == 'pop_back'):
        if(len(deque)>0):
            print(deque.pop())
        else:
            print(-1)
    if(command == 'size'):
        print(len(deque))
    if(command == 'empty'):
        if(len(deque) == 0):
            print(1)
        else:
            print(0)
    if(command == 'front'):
        if(len(deque)>0):
            print(deque[0])
        else:
            print(-1)
    if(command == 'back'):
        if(len(deque)>0):
            print(deque[-1])
        else:
            print(-1)

