from itertools import combinations_with_replacement

N,M = map(int, input().split())
arr = list(range(1,N+1))
# 중복을 허용하는 조합
for case in combinations_with_replacement(arr, M):
    print(' '.join(map(str, case)))