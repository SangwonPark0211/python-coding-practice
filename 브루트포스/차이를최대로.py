def next_permutation(arr):

    n = len(arr)-1
    i = n
    # 중복된 원소 있을 수 있으므로 부등호에 =를 포함시켜 주어야 함
    while arr[i-1] >= arr[i]:
        i -= 1

    j = i-1
    diff = 10000
    position_to_switch = 0

    # select the number to chage position
    for k in range(i, n+1):
        if arr[k]-arr[j] > 0:
            diff = min(diff, arr[k]-arr[j])
    for m in range(i, n+1):
        if arr[m]==arr[j]+diff:
            position_to_switch = m
            break

    # change position of two number
    temp = arr[j]
    arr[j] = arr[position_to_switch]
    arr[position_to_switch] = temp

    temp_list = arr[j+1:]
    temp_list.sort()
    arr = arr[:j+1]
    arr = arr + temp_list

    return arr

if __name__=='__main__':

    num = int(input())
    arr = []
    arr = list(map(int, input().split()))
    arr.sort()

    # the number of permutation
    per_num = 1
    for i in range(num):
        per_num *= (i+1)
    per_num
    per_num = per_num - 1

    # calculate for the first list
    sum_list = []
    temp_sum = 0
    for i in range(num-1):
        temp_sum += abs(arr[i] - arr[i+1])
    sum_list.append(temp_sum)
    

    for _ in range(per_num):
        temp_sum = 0
        arr = next_permutation(arr)
        
        for i in range(num-1):
            temp_sum += abs(arr[i] - arr[i+1])
        sum_list.append(temp_sum)

    print(max(sum_list))