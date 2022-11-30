code = input()
code = list(map(int,str(code)))
dp = [1]*len(code)
flag = 0
if(code[0]==0): flag=1
if(len(code)>1):
    if(code[0]>2 and code[1]==0):flag=1
    elif(code[1] == 0 ):dp[1] = 1
    elif(code[0]*10+code[1]>10 and code[0]*10+code[1]<27): dp[1] = 2
    else : dp[1] = 1
for i in range (2,len(code)):
    if(code[i-1]>2 and code[i]==0):flag=1
    if(code[i-1]==0 and code[i]==0):flag = 1
    elif(code[i]==0):dp[i]=dp[i-2]
    elif(code[i-1]==0):dp[i]=dp[i-1]
    elif(code[i-1]*10+code[i]<27):dp[i] = dp[i-2]+dp[i-1]
    else :dp[i] = dp[i-1]
if(flag == 1): print(0)
else : print(dp[len(code)-1]%1000000)