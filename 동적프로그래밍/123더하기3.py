# 백준 15988

t = int(input())
dp = [0]*(1000001)
dp[1],dp[2],dp[3]=1,2,4
for i in range(4, 1000001):
    dp[i] = ((dp[i-1] + dp[i-2]) %1000000009 + dp[i-3]) % 1000000009
for _ in range(t):
    n = int(input())
    if n==1:
        print(dp[1])
        continue
    elif n==2:
        print(dp[2])
        continue
    elif n==3:
        print(dp[3])
        continue
    print(dp[n])