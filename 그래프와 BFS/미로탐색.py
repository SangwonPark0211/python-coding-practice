from queue import PriorityQueue as pq
def dijkstra(): 
    heap = pq() 
    heap.put((1, (0, 0))) 
    crush[0][0] = 0 
    # 상하좌우
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 
    while True:
        cnt, (hi, hj) = heap.get() 
        # print(cnt, hi, hj)
        if hi == n-1 and hj == m-1:
            break
        for d in range(4):
            x, y = hi + dx[d], hj + dy[d]
            if 0<=x<n and 0<=y<m and crush[x][y]<0:
                # crush[x][y] = (x,y)전까지 부순 벽의 갯수
                crush[x][y] = cnt
                if maze[x][y] == '1':
                    # heap의 원소의 cnt = (x,y)에서 부순 벽의 갯수도 포함
                    heap.put((cnt+1, (x, y)))
                    
n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
crush = [[-1] * m for _ in range(n)]
dijkstra()
print(crush[n-1][m-1]+1)

