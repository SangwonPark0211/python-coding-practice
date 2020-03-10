from itertools import product

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
result = set(result)
for case in product(arr, repeat=M):
    if case not in result:
        result.add(case)
        print(' '.join(map(str, case)))