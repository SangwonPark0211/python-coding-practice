def next_permutation(arr):

    n = len(arr)-1
    if n==0:
        return -1
    i = n
    while arr[i-1] > arr[i]:
        i -= 1
        if i == 0:
            return -1

    j = i-1
    diff = 10000
    position_to_switch = 0
    for k in range(i, n+1):
        if arr[k]-arr[j] > 0:
            diff = min(diff, arr[k]-arr[j])
    for m in range(i, n+1):
        if arr[m]==arr[j]+diff:
            position_to_switch = m
            break
    temp = arr[j]
    arr[j] = arr[position_to_switch]
    arr[position_to_switch] = temp
    temp_list = arr[j+1:]
    temp_list.sort()
    arr = arr[:j+1]
    arr = arr + temp_list
    #arr[j+1:].sort()
    return arr

if __name__=='__main__':

    num = int(input())
    arr = []
    for i in range(num):
        arr.append(i+1)
    total_trial = 1
    for i in range(num):
        total_trial *= i+1
    for i in range(total_trial):
        for j in range(num):
            print(arr[j], end=' ')
        print('\n', end='')
        arr = next_permutation(arr)


