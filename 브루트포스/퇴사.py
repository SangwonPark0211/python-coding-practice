
n = int(input())
t = []
p = []
dp = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)

for i in range(n-1,-1,-1):
    if i+t[i]>n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i]+dp[i+t[i]])

print(dp[0])

"""
특이점
1. 겹치지 않기 위해 dp를 뒤에서부터 순차적으로 탐색하며 갱신
2. range(n-1,-1,-1)처럼 쓰면 뒤에서부터 역순으로 참조. 여기서 2nd인자인 -1은 미포함
3. a, b = list는 list의 원소 하나씩 a, b에 대응(단 원소갯수와 변수갯수가 일치해야!!!)
"""


    
        
    
