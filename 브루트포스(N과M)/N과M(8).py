from itertools import combinations_with_replacement

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for case in combinations_with_replacement(arr, M):
    print(' '.join(map(str, case)))