import sys

M,N = 0, 0
arr = []
cnt = 0

def dfs(x,y):
    arr[x][y]=0
    if arr[x - 1][y] == 1:
        dfs(x - 1, y)
    if arr[x + 1][y] == 1:
        dfs(x + 1, y)
    if arr[x][y - 1] == 1:
	    dfs(x, y - 1)
    if arr[x][y + 1] == 1:
	    dfs(x, y + 1)
    if arr[x-1][y-1] == 1:
        dfs(x-1, y-1)
    if arr[x-1][y+1] == 1:
        dfs(x-1, y+1)
    if arr[x+1][y-1] == 1:
        dfs(x+1, y-1)
    if arr[x+1][y+1] == 1:
        dfs(x+1, y+1)

    return


if __name__=='__main__':
    # 파이썬의 경우 재귀호출의 깊이 limit을 설정해주어야 런타임에러가 나지 않는다. 인자는 최대재귀호출 횟수
    sys.setrecursionlimit(10**8)
    while True:
        cnt = 0
        input_arr = []
        M,N = map(int, sys.stdin.readline().split())
        if M==0 and N==0:
            break
        temp = []
        for _ in range(M+2):
            temp.append(0)
        for _ in range(N+2):
            # 리스트를 복사해주어야 함!!! ref by value
            arr.append(temp[:])


        for _ in range(N):
            input_arr.append(list(map(int, sys.stdin.readline().split())))

        for i in range(N):
            for j in range(M):
                arr[i+1][j+1] = input_arr[i][j]        

        for i in range(1, N+1):
            for j in range(1, M+1):
                if arr[i][j] == 1:
                    dfs(i,j)
                    cnt += 1

        print(cnt)
        del arr[:]
        


