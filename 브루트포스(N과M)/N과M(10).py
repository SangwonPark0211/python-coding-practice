from itertools import combinations

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
for case in combinations(arr, M):
    result.append(' '.join(map(str, case)))
already_printed = []
for i in result:
    if i not in already_printed:
        print(i)
        already_printed.append(i)