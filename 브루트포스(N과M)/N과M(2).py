from itertools import combinations

N, M = map(int, input().split())
arr = list(range(1,N+1))

for case in combinations(arr, M):
    print(' '.join(map(str, case)))