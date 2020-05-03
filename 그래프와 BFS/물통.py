# BOJ 2251
from collections import deque

def pour(x,y):
    if not visit[x][y]:
        visit[x][y]=True
        q.append((x,y))

def bfs():
    q.append((0,0)) #처음 시작 상태
    visit[0][0]=True
    while q:
        x,y=q.popleft()
        z=c-x-y
        if x==0:
            ans.append(z)
        # 물 옮기는 6가지 경우(x->y,x->z,y->x,y->z,z->x,z->y)
        water=min(x,b-y)
        pour(x-water,y+water)
        water=min(x,c-z)
        pour(x-water,y)
        water=min(y,a-x)
        pour(x+water,y-water)
        water=min(y,c-z)
        pour(x,y-water)
        water=min(z,a-x)
        pour(x+water,y)
        water=min(z,b-y)
        pour(x,y+water)

a,b,c=list(map(int, input().split()))
q = deque()
ans = []
visit = [[False]*(b+1) for _ in range(a+1)]
bfs()
ans.sort()
print(' '.join(map(str, ans)))

