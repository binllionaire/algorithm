size = int(input())
A = list(map(int,input().split()))
increase = [1]*size
decrease = [1]*size
result = [0]*size

for i in range(size):
    for j in range(i):
        if(A[i] > A[j] and increase[i] < increase[j]+1):
            increase[i] = increase[j]+1

for i in range(size-1,-1,-1):
    for j in range(i+1,size):
        if(A[i] > A[j] and decrease[i] < decrease[j]+1):
            decrease[i] = decrease[j]+1
    result[i] = decrease[i]+increase[i]-1

print(max(result))
