N = int(input())
num = list(map(int,input().split()))
count = 0 
for i in range(N): 
    temp = 0  
    for j in range(1,num[i]):
        if(num[i]%j == 0):
            temp += 1
    if(temp == 1):
        count += 1
print(count)