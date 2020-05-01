# BOJ 1644

n = int(input())
prime = [1]*(n+1)
for i in range(2, n+1):
    if prime[i]:
        t=2
        while i*t<=n:
            prime[i*t]=0
            t+=1
ans = 0
for i in range(n, 1, -1):
    if prime[i]:
        tmp = 0
        for j in range(i, 1, -1):
            if prime[j]:
                tmp+=j
                if tmp==n:
                    ans+=1
                    break
                elif tmp>n:
                    break
print(ans)
    