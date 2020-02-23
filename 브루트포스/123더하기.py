# dp = [0]*11
# dp.append(0)
# dp.append(1)
# dp.append(2)
# dp.append(4)
# dp[0], dp[1], dp[2], dp[3] = 0,1,2,4
# for i in range(4, 11):
#     dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    
# trial = int(input())

# for i in range(trial):
#     num = int(input())
#     print(dp[num])

dp = [1,2,4]
for i in range(4,11):
    dp.append(sum(dp[-3:]))

trial = int(input())

for i in range(trial):
    num = int(input())
    print(dp[num-1])