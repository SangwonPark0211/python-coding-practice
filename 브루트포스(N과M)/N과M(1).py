from itertools import permutations

N, M = map(int, input().split())
arr = list(range(1, N+1))

for case in permutations(arr, M):
    print(' '.join(map(str, case)))
    

