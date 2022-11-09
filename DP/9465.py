T=int(input())
for _ in range(0,T):
  n=int(input())
  sticker = [list(map(int,input().split())) for _ in range(2)]
  dp = [[0]*n for i in range(2)]
  dp[0][0] = sticker[0][0]
  dp[1][0] = sticker[1][0]
  for j in range(1,n):
    for i in range(0,2):
      if(i==0):
        dp[i][j] = dp[1][j-1] + sticker[i][j]
        if((sticker[i][j]+dp[1][j-1] < sticker[i][j] + max(dp[i][j-2],dp[i+1][j-2]) and j >= 2)):
          dp[i][j] = sticker[i][j] + max(dp[i][j-2],dp[i+1][j-2])
      elif(i==1):
        dp[i][j] = dp[0][j-1] + sticker[i][j]
        if((sticker[i][j]+dp[0][j-1] < sticker[i][j] + max(dp[i][j-2],dp[i-1][j-2]) and j >= 2)):
          dp[i][j] = sticker[i][j] +max(dp[i][j-2],dp[i-1][j-2])
  print(max(dp[0][n-1],dp[1][n-1]))   
