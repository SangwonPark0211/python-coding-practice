import queue

n = int(input())
d = [[-1]*1001 for i in range(1001)]
d[1][0] = 0
q = queue.Queue()
q.put((1,0))

while q.qsize():
    s, c = q.get()

    # 복사
    if d[s][s]==-1:
        d[s][s]=d[s][c]+1
        q.put((s,s))
    # 붙여넣기
    if s+c<=n and d[s+c][c]==-1:
        d[s+c][c]=d[s][c]+1
        q.put((s+c,c))
    # 삭제
    if s-1>=0 and d[s-1][c]==-1:
        d[s-1][c]=d[s][c]+1
        q.put((s-1,c))

# 화면에 이모티콘이 n개이면서 클립보드에 있는 이모티콘 수가 0~n-1개 일때 중에서 최솟값
ans=-1
for i in range(n):
    if d[n][i]!=-1:
        if ans==-1 or ans>d[n][i]:
            ans=d[n][i]
print(ans)