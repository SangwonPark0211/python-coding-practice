E_max = 15
S_max = 28
M_max = 19

a = list(map(int, input().split()))
E, S, M = a[0], a[1], a[2]
year = 0
x, y, z = 0, 0, 0
while True:
    if(x==E and y==S and z==M):
        break
    x = x%E_max + 1
    y = y%S_max + 1
    z = z%M_max + 1
    year+=1
    
print(year)

