N = int(input())
dp = [1]*(N+1)
for i in range(1,N+1):
    dp[i] = dp[i-1] * i
pac = list(str(dp[N]))
count = 0
for i in range(len(pac)-1,0,-1):
    if(pac[i] == '0'):
        count += 1
    else:
        break
print(count)