# BOJ 9376

from collections import deque

def bfs(x,y):
    dist = [[-1]*(w+2) for _ in range(h+2)]   # 방문체크하고 갱신하기 위한 용도
    q = deque()
    q.append((x,y))
    dist[x][y]=0
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx > h+1 or ny < 0 or ny > w+1:
                continue
            if dist[nx][ny]>=0 or maze[nx][ny]=='*':
                continue
            if maze[nx][ny]=='#':
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
            elif maze[nx][ny]=='.':
                dist[nx][ny]=dist[x][y]
                q.appendleft((nx,ny))

    return dist


for _ in range(int(input())):
    h, w = map(int, input().split())
    maze=[]
    maze.append(list('.'*(w+2)))
    for _ in range(h):
        maze.append(list('.'+input().strip()+'.'))
    maze.append(list('.'*(w+2)))
    dq = deque()
    for i in range(h+2):
        for j in range(w+2):
            if maze[i][j]=='$':
                maze[i][j]='.'
                dq.append((i,j))
    sx, sy = dq.popleft()
    d1 = bfs(sx, sy)
    sx, sy = dq.popleft()
    d2 = bfs(sx, sy)
    d3 = bfs(0, 0)
    ans = 1000000000
    for i in range(h+2):
        for j in range(w+2):
            if maze[i][j]=='*':
                continue
            k = d1[i][j] + d2[i][j] + d3[i][j]
            if maze[i][j]=='#':
                k-=2
            ans = min(k,ans)

    print(ans)