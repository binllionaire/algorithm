N=int(input())
dp= [0]*(N+1)
dp[1]=9
dp[2]=17
for i in range(3,N+1):
  dp[i]=dp[i-2]+dp[i-1]-1
print(dp[i]%1000000000)