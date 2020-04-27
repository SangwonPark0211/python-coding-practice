# 백준 11055
import sys

N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N
if N == 1:
    print(arr[0])
    sys.exit()
dp[0]=arr[0]
for i in range(1,N):
    s = []
    for j in range(i-1,-1,-1):
        if arr[j]<arr[i]:
            s.append(arr[i]+dp[j])
    if s:
        dp[i]=max(s)
    else:
        dp[i]=arr[i]
print(max(dp))
print(dp)
