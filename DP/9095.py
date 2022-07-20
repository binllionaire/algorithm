# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

T=int(input())

for i in range(0,T) :
  n=int(input())
  dp = [0] * 12
  dp[1]=1
  dp[2]=2
  dp[3]=4

  if(n>3) :
    for j in range(4,12) :
        dp[j] = dp[j-1] + (dp[j-2]) + dp[j-3]

  print(dp[n])
  