# 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다.
# 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
# 모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
# 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을 작성하시오.

T=int(input())
for i in range(0,T) :
  n=int(input())
  dp = [list(map(int, input().split()))for _ in range(2)]
  dp[0][1] += dp[1][0]
  dp[1][1] += dp[0][0]
  for  i in range(2,n+1):
      dp[0][i] += max(dp[1][i-1],dp[1][i-2])
      dp[1][i] += max(dp[0][i-1],dp[0][i-2])
  print(max(dp[0][n-1],dp[1][n-1]))
  
    