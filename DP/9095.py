T=int(input())
for T in range (0,T):
  n=int(input())
  dp = [1]*11
  dp[1]=1
  dp[2]=2
  for i in range(3,n+1):
      dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
  print(dp[n])