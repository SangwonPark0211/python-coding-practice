# BOJ 14889

import itertools
import sys

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
member = [i for i in range(n)]
gap = sys.maxsize
tt = list(itertools.combinations(member, n//2))
for team1 in tt:
    sum1, sum2 = 0, 0
    team2 = [x for x in member if x not in team1]
    for x, y in (itertools.combinations(team1, 2)):
        sum1 += mat[x][y] + mat[y][x]
    for x, y in (itertools.combinations(team2, 2)):
        sum2 += mat[x][y] + mat[y][x]
    gap = min(gap, abs(sum1-sum2))
print(gap)
