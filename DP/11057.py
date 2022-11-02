N=int(input())
dp = [[0]*10 for i in range(N+1)]
total=0
for i in range(0,N):
  row_sum = 0
  for j in range(0,10):
    if(i==0):
      dp[i][j]=1
    else:
      if(j==0):
        for k in range(0,10):
          row_sum+=dp[i-1][k]
        dp[i][j]=row_sum
      else:
        dp[i][j]=dp[i][j-1]-dp[i-1][j-1]
for i in range (0,10):
  total+=dp[N-1][i]
print(total%10007)