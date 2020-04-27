# 백준 11057

n = int(input())
arr = [[0]*10 for _ in range(1001)]
for i in range(10):
    arr[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            arr[i][j] += arr[i-1][k]
print(sum(arr[n])%10007)