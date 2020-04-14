# 백준 3055

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def move(x,y):
    global stop
    SET = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if board[x][y] == '*':  # 물
                if  board[nx][ny] == '.'or board[nx][ny] == 'G':
                    board[nx][ny] = '*'

            # S-> D
            if board[x][y] == 'S':# 비버
                if board[nx][ny]=='.':  # 이동
                    SET =True
                    board[nx][ny] = 'S'
                    record[nx][ny] = record[x][y] + 1

                if board[nx][ny]=='D': # 종료
                    record[nx][ny] = record[x][y] + 1
                    stop = True
                    print(record[nx][ny])
                    break

    # 이동한 칸 표시
    if SET:
        board[x][y] = 'G'

M, N = map(int, input().split())
board = [list(input()) for _ in range(M)]
record = [[0]*N for i in range(M)]
stop = False
count = M*N
while not stop:
    # 매 싸이클마다 초기화되는 두 리스트
    water_lst = []
    dudu_lst = []
    for i in range(M):
        for j in range(N):
            if board[i][j]=='*':
                water_lst.append((i,j))

            if board[i][j]=='S':
                dudu_lst.append((i,j))

    for p in water_lst:
        move(p[0], p[1])

    for p in dudu_lst:
        move(p[0],p[1])
        if stop:
            break

    count -= 1
    if count <0:
        print('KAKTUS')
        break
