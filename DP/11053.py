N=int(input())
A = list(map(int, input().split()))
dp = [1]*N
for i in range (1,len(A)):
  temp = [1]
  maxnum=0
  for j in range(0,i):
    if(A[j]<A[i]):
      temp.append(dp[j]+1)
  dp[i] = max(temp)
print(max(dp))