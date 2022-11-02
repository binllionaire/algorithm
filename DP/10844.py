N=int(input())
dp = [[0]*10 for i in range(N+1)]
total = 0 

for i in range(0,N):
  for j in range (0,10):
    if(i==0):
      dp[i][j]=1
    else:
      if(j==0):
        dp[i][j]=dp[i-1][j+1]
      elif(j==9):
        dp[i][j]=dp[i][0]
      elif(j<9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]

for i in range(1,10):
  total+=dp[N-1][i]
print(total%1000000000)