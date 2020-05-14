# BOJ 13913

from collections import deque
import sys

N,K = list(map(int, input().split()))
visit = [-1]*100001
if N==K:
    print(0)
    print(N)
    sys.exit()

def bfs():
    while q:
        x = q.popleft()
        if x==K:
            break
        if 0<=x-1<=100000 and visit[x-1]==-1:
            q.append(x-1)
            visit[x-1]=x
        if 0<=x+1<=100000 and visit[x+1]==-1:
            q.append(x+1)
            visit[x+1]=x
        if 0<=2*x<=100000 and visit[2*x]==-1:
            q.append(2*x)
            visit[2*x]=x

visit[N] = -2    #시작지점
q = deque()
q.append(N)
bfs()
i=K
result = []
while visit[i]!=-2:
    result.append(i)
    i=visit[i]
result.reverse()
print(len(result))
ans = [N]+result
print(' '.join(map(str, ans)))
