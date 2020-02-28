# 출처 https://daimhada.tistory.com/94
import sys
from itertools import combinations
#input = sys.stdin.readline

flag = True

while flag:
    line = list(map(int, input().split()))
    n = int(line[0])
    if n == 0:
        flag = False
        break

    for case in combinations(line[1:], 6):
        print(' '.join(map(str,case)))
    print('')

"""
1. 파이썬 내장 itertools의 combinations와 permutations 메서드
2. ' '.join() 함수 사용법
"""