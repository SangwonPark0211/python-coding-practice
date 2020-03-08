from itertools import product

N,M = map(int, input().split())
arr = list(range(1,N+1))
# 중복을 허용하는 순열
for case in product(arr, repeat=M):
    print(' '.join(map(str, case)))