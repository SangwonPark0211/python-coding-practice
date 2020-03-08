from itertools import product

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for case in product(arr, repeat=M):
    print(' '.join(map(str, case)))