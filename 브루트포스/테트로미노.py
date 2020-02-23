N, M = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
set_of_sum = []

def square_shape():
    for i in range(N-1):
        for j in range(M-1):
            sum = arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]
            set_of_sum.append(sum)

def I_shape():
    for i in range(N):
        for j in range(M-3):
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3]
            set_of_sum.append(sum)
    for j in range(M):
        for i in range(N-3):
            sum = arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j]
            set_of_sum.append(sum)

def L_shape():
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1]
            set_of_sum.append(sum)
    for i in range(N-1):
        for j in range(M-2):
            sum = arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i][j+2]
            set_of_sum.append(sum)
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]
            set_of_sum.append(sum)
    for i in range(N-1):
        for j in range(M-2):
            sum = arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]
            set_of_sum.append(sum)
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+2][j]
            set_of_sum.append(sum)
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]
            set_of_sum.append(sum)
    for i in range(N-1):
        for j in range(M-2):
            sum = arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]
            set_of_sum.append(sum)
    for i in range(N-1):
        for j in range(M-2):
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+2]
            set_of_sum.append(sum)

def S_shape():
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1]
            set_of_sum.append(sum)
    for i in range(N-1):
        for j in range(M-2):
            sum = arr[i][j+1]+arr[i][j+2]+arr[i+1][j]+arr[i+1][j+1]
            set_of_sum.append(sum)
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j]
            set_of_sum.append(sum)
    for i in range(N-1):
        for j in range(M-2):
            sum  = arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j+2]
            set_of_sum.append(sum)

def T_shape():
    for i in range(N-1):
        for j in range(M-2):
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]
            set_of_sum.append(sum)
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]
            set_of_sum.append(sum)
    for i in range(N-1):
        for j in range(M-2):
            sum = arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]
            set_of_sum.append(sum)
    for i in range(N-2):
        for j in range(M-1):
            sum = arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j]
            set_of_sum.append(sum)

if __name__=='__main__':

    square_shape()
    I_shape()
    L_shape()
    S_shape()
    T_shape()

    print(max(set_of_sum))
