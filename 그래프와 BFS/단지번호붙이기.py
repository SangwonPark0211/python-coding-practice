import sys

def dfs(cnt, x, y, arr):

    arr[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if 0<=n_x<N and 0<=n_y<N:
            if arr[n_x][n_y] == 1:
                cnt = dfs(cnt+1, n_x, n_y, arr)

    return cnt


N = int(sys.stdin.readline())
ans = []
arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans.append(dfs(1, i, j, arr))

print(len(ans))
for house in sorted(ans):
    print(house)

