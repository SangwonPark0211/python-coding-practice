from itertools import combinations_with_replacement

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
result = set(result)
for case in combinations_with_replacement(arr, M):
    if case not in result:
        result.add(case)
        print(' '.join(map(str, case)))