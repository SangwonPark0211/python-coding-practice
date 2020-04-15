# 백준 16194

N = int(input())
card = [0]
card += list(map(int, input().split()))
# dp[i]의 값은 i개의 카드를 구매하는데 필요한 최소비용
dp = [0] * (N+1)
dp[1] = card[1]
dp[2] = min(card[1]*2, card[2])
for i in range(3, N+1):
    dp[i] = card[i]
    for j in range(1, i//2+1):
        dp[i] = min(dp[i], dp[j]+dp[i-j])

print(dp[N])