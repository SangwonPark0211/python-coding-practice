from itertools import permutations

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
for case in permutations(arr, M):
    result.append(' '.join(map(str, case)))
result = set(result)
result = list(result)
result.sort()
for i in result:
    print(i)