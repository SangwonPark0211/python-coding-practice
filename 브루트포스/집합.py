import sys

N = int(input())
S = {}
S = set()
for _ in range(N):
    line = sys.stdin.readline().split()
    
    if line[0]=='add':
        S.add(line[1])
        continue
    elif line[0]=='remove':
        S.discard(line[1])
        continue
    elif line[0]=='check':
        if line[1] in S:
            print(1)
            continue
        else:
            print(0)
            continue
    elif line[0]=='toggle':
        if line[1] in S:
            S.remove(line[1])
            continue
        else:
            S.add(line[1])
            continue
    elif line[0]=='all':
        S.update(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
        continue
    elif line[0]=='empty':
        S = {}
        S = set()
    