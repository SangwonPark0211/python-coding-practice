from itertools import permutations

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for case in permutations(arr, M):
    print(' '.join(map(str, case)))