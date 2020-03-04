from itertools import permutations
from itertools import combinations

L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()
moeum_list = ['a', 'e', 'i', 'o', 'u']
for case in combinations(alphabet, L):
    moeum = 0
    jaeum = 0
    for i in range(len(case)):
        if case[i] in moeum_list:
            moeum += 1
        else:
            jaeum += 1
    if moeum>0 and jaeum>1:
        print(''.join(map(str, case)))
