# 백준 1699
import sys

n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    j=1
    while j*j<=i:
        if dp[i]>dp[i-j*j]+1:
            dp[i]=dp[i-j*j]+1
        j+=1
print(dp[n])
