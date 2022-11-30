T=int(input())
for i in range(T):
    N=int(input())
    dp = [1]*N
    for i in range(3,N):
        dp[i] = dp[i-3]+dp[i-2]
    print(dp[N-1])
