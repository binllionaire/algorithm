size = int(input())
A = list(map(int, input().split()))
dp =[0]*1000
dp[0] = A[0]
for i in range (1,size):
    temp = [0]
    for j in range(0,i):
        if(A[j]<A[i]):
            temp.append(dp[j])
    dp[i] = max(temp)+A[i]
print(max(dp))
