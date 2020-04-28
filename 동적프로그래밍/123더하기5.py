# 백준 15990

t = int(input())
dp = [[0]*4 for _ in range(100001)]

# dp[i][j] : i를 만드는 데 더해지는 끝 수가 j인 경우의 수
dp[1][1] = 1
dp[2][2] = 1
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

for i in range(4, 100001):
    for j in range(1, 4):
        dp[i][j] = ((dp[i-j][1]+dp[i-j][2])%1000000009 + dp[i-j][3])%1000000009 - dp[i-j][j]

for _ in range(t):
    n = int(input())
    print(((dp[n][1]+dp[n][2])%1000000009+dp[n][3])%1000000009)
    
