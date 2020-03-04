from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for case in list(combinations(arr, i+1)):
        if sum(case) == S:
            cnt+=1
print(cnt)