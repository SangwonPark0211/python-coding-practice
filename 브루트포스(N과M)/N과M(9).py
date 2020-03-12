from itertools import permutations

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
result = set(result)
for case in permutations(arr, M):
    if case not in result:
        result.add(case)
        print(' '.join(map(str, case)))

# result를 list로 두고 for문 돌렸을 땐 시간초과->set으로 바꾸니 해결
# 이유는 list의 경우 x가 있는지 리스트의 끝가지 비교하는 최악의 경우 O(n)이지만
# set의 경우 비교하는 원리가 hash table과 같아서(즉, set은 리스트와 달리 순서가 없고 원소들이 key값과 같은 셈이다.)