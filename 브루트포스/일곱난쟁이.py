dwarf = []
for _ in range(9):
    height = int(input())
    dwarf.append(height)
sum = 0
for i in dwarf:
    sum+=i
for i in range(8):
    for j in range(i+1,9):
        if sum-dwarf[i]-dwarf[j]==100:
            del dwarf[i]
            del dwarf[j-1]
            break
    if len(dwarf)==7:
        break
dwarf.sort()
for i in dwarf:
    print(i)

# 다른 스타일2)
# a=[]
# for i in range(9):
#     a.append(int(input()))
# res=sum(a)
# a.sort()
# for i in range(9):
#     for j in range(i+1,9):
#         if res-a[i]-a[j]==100:
#             for k in range(9):
#                 if k==i or k==j:
#                     continue
#                 else:
#                     print(a[k])
        