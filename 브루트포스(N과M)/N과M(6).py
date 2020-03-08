from itertools import combinations

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for case in combinations(arr, M):
    print(' '.join(map(str, case)))