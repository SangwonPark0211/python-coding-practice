# import sys

# N, M = 0, 0
# arr = []
# visit = []
# cnt = 0

# def dfs(x):

#     if visit[x] == 1:
#         return
#     visit[x] = 1
#     for i in range(N):
#         if arr[x][i] == 1:
#             dfs(i)


# if __name__=='__main__':

#     sys.setrecursionlimit(10**8)
#     # N은 정점, M은 간선의 갯수
#     N, M = map(int, sys.stdin.readline().split())
#     arr = [[] for i in range(N)]
#     visit = [0] * N

#     for i in range(N):
#         arr[i] = visit[:]

#     for _ in range(M):
#         u, v = map(int, sys.stdin.readline().split())
#         arr[u-1][v-1] = 1
#         arr[v-1][u-1] = 1

#     for i in range(N):
#         if visit[i] == 0:
#             dfs(i)
#             cnt += 1

#     print(cnt)
def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
            
N, M = map(int, input().split())
adj = [[] for i in range(N+1)]
visited = [False] * (N + 1)
cnt = 0
 
for i in range(M):
    input_data = list(map(int, input().split()))
    adj[input_data[0]].append(input_data[1])
    adj[input_data[1]].append(input_data[0])
    
for i in range(1, len(visited)):
    if not(visited[i]):
        cnt += 1
        dfs(i)
        
print(cnt)
    
        