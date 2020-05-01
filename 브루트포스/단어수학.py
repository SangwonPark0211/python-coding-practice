# BOJ 1339

t = int(input())
lst = []
for i in range(t):
    lst.append(input())
alpha = [0]*26
for num in lst:
    for i in range(len(num)):
        alpha[ord(num[i])-ord('A')] += 10**(len(num)-i-1)
alpha.sort(reverse=True)
ans=0
for i in range(9,-1,-1):
    ans+=alpha[9-i]*i
print(ans)